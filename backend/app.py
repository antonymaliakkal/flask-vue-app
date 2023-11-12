# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_security import Security, SQLAlchemyUserDatastore, login_required, UserMixin, RoleMixin

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'thisisasecret'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SECURITY_PASSWORD_SALT'] = 'thisisasecretsalt'

# db = SQLAlchemy(app)

# roles_users = db.Table('roles_users',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('role_id', db.Integer, db.ForeignKey('role.id')))

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(255))
#     active = db.Column(db.Boolean)
#     confirmed_at = db.Column(db.DateTime)

# class Role(db.Model, RoleMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40))
#     description = db.Column(db.String(255))

# # user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# # security = Security()
# # security.init_app(app, user_datastore)

# if __name__ == '__main__':
#     app.run(debug = True)


# with app.app_context():
#     db.create_all() 




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
CORS(app)


app.config['SECRET_KEY'] = 'thisisasecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


from routes import*
from models import*


if __name__ == '__main__':
    app.run(debug = True)


with app.app_context():
   db.create_all() 