from celery import Celery, Task
from flask import Flask, render_template
from celery.schedules import crontab
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db_instance import db
from models import User, Orders, OrderProducts, Product
from datetime import datetime, timedelta, date
from flask_mail import Mail,Message
import calendar 

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

    today = date.today()    
    first = today.replace(day=1)
    last_month_end = first - timedelta(days=1)
    no_days = calendar.monthrange(last_month_end.year, last_month_end.month)[1]
    last = last_month_end.replace(day= no_days)
    last_month_beg = last - timedelta(days=(no_days - 1))

    for user in users:
        formatted_orders = {}
        orders = Orders.query.filter(Orders.date >= last_month_beg, Orders.date <= last_month_end, Orders.order_user == user.id).all()
        for order in orders:
            orders = OrderProducts.query.filter_by(order_id=order.order_id).all()
            formatted_orders[order.date] = orders

        sendOrderSummary(user, formatted_orders)

 
def sendChat(user):
    msg = Message(subject='Great deals exclusively for you!', sender='info@priyammart.com', recipients=[user.username])
    msg.body = "Hey {}, There are exclusive offer for you. Come buy!".format(user.username)
    mail.send(msg)

def sendOrderSummary(user, orders):
    msg = Message(subject='Your monthly report', sender='info@priyammart.com', recipients=[user.username])
    msg.html = create_html(user, orders)
    mail.send(msg)

def create_html(user, orders):
    order_list = []
    for (date,order) in orders.items():
        o = {}
        o['items'] = []
        total = 0
        # orderDict = json.loads(orders)
        for i in order:
            d = {}
            d['name'] = i.product.name
            d['rate'] = i.product.price
            d['units'] = i.quantity
            d['price'] = i.product.price*i.quantity
            o['items'].append(d)
            total+=d['price']
        o['total'] = total
        o['date'] = date
        order_list.append(o)
    return render_template('order_summary.html', name=user.username,orders=order_list)


def create_csv():
    csv = ''
    csv+="Name,Price,Units Remaining\n"
    ps = Product.query.all()
    for p in ps:
        csv+=p.name
        csv+=','
        csv+=str(p.price)
        csv+=','
        csv+=str(p.stock)
        csv+="\n"
    return csv



@celery_app.task
def sendProductSummary(email):
    sender_email = "info@priyammart.com"
    receiver_email = email
    msg = Message(subject='Your monthly report', sender=sender_email, recipients=[receiver_email])
    msg.body = 'Here is you product summary,'
    csv = create_csv()

    msg.attach('product_summary.csv', 'text/csv', csv.encode())

    mail.send(msg)