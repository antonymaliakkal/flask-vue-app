from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_redis import FlaskRedis



app = Flask(__name__)
CORS(app)


app.config['SECRET_KEY'] = 'thisisasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'  
app.config['REDIS_URL'] = 'redis://localhost:6379'
app.config['REDIS_DB'] = 0



db = SQLAlchemy(app)
jwt = JWTManager(app)
redis_store = FlaskRedis(app)


from routes import*
from models import*


if __name__ == '__main__':
    app.run(debug = True)


with app.app_context():
    db.create_all() 
    user = User.query.filter_by(role='admin').all()
    if user == []:
        user = User(username = "admin", password = "admin", role = "admin")
        db.session.add(user)
        db.session.commit()