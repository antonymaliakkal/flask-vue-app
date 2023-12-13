from models import User

from celery_app import app
from db_instance import db
from flask_redis import FlaskRedis



app.config['REDIS_URL'] = 'redis://localhost:6379'
app.config['REDIS_DB'] = 0


redis_store = FlaskRedis(app)


with app.app_context():
    db.create_all() 
    user = User.query.filter_by(role='admin').all()
    if user == []:
        user = User(username = "admin", password = "admin", role = "admin")
        db.session.add(user)
        db.session.commit()

import routes
