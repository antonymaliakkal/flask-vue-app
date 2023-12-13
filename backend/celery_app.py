from celery import Celery, Task
from flask import Flask
from celery.schedules import crontab
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db_instance import db
from models import User, Orders, OrderProducts
from datetime import datetime
from flask_mail import Mail,Message


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app


app = Flask(__name__)
CORS(app)

app.config.from_mapping(
    JWT_SECRET_KEY = 'jwt_secret_key' , 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db',
    SECRET_KEY = 'thisisasecret',
    CELERY=dict(
        broker_url="redis://localhost",
        result_backend="redis://localhost",
        task_ignore_result=True,
    ),
)

app.config['MAIL_SERVER']='smtp-relay.brevo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '21f1005345@ds.study.iitm.ac.in'
app.config['MAIL_PASSWORD'] = 'dqwkBmRaH95fAgtp'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

db = db.init_app(app)
jwt = JWTManager(app)

celery_app = celery_init_app(app)
celery_app.conf.timezone = 'Asia/Kolkata'
print(celery_app, 'sljdnasjknd')

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(hour=17, minute=00),
        sendChatTask.s(),
    )

    sender.add_periodic_task(
        crontab(0, 0, day_of_month='1'),
        monthylReportTask.s(),
    )

@celery_app.task
def sendChatTask():
    users = User.query.filter_by(role='user').all()
    t = datetime.now()
    for user in users:
        time = t - user.last_visited
        if time.total_seconds() > 1:
            sendChat(user)

@celery_app.task
def monthylReportTask():
    users = User.query.filter_by(role='user').all()
    for user in users:
        orders = Orders.query.filter(Orders.order_date <= 10, Orders.order_user == user.id).all()
        for i in orders:
            print(i)

 
def sendChat(user):
    msg = Message(subject='Great deals exclusively for you!', sender='info@priyammart.com', recipients=[user.email])
    msg.body = "Hey {}, There are exclusive offer for you. Come buy!".format(user.username)
    mail.send(msg)
