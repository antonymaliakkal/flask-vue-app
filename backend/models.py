from app import db
from sqlalchemy import*

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50) , nullable = False)
    role = db.Column(db.String(20),nullable=False)

class Manager_request(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , ForeignKey(User.id))

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200))

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    cat_id = db.Column(db.Integer , ForeignKey(Category.id))
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)

class Cart(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer , ForeignKey(User.id))
    product_id = db.Column(db.Integer , ForeignKey(Product.id))
    quantity = db.Column(db.Integer)

class Orders(db.Integer):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer , ForeignKey(User.id))
    product_id = db.Column(db.Integer , ForeignKey(Product.id))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

