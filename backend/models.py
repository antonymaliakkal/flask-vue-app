from db_instance import db
from sqlalchemy import*
from enum import Enum

class StatusEnum(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PENDING = 'pending'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(50) , nullable = False)
    role = db.Column(db.String(20),nullable=False)
    last_visited = db.Column(db.DateTime(timezone=True), server_default=func.now())


class Manager_request(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , ForeignKey(User.id))

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200))

class CategoryRequest(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200))
    status = db.Column(db.Enum(StatusEnum), default=StatusEnum.PENDING)

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

class Orders(db.Model):
    order_id = db.Column(db.Integer , primary_key=True)
    order_user = db.Column(db.Integer , ForeignKey(User.id))
<<<<<<< HEAD
    date = db.Column(db.TIMESTAMP, server_default=func.now())

class OrderProducts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer , ForeignKey(Orders.order_id))
    product_id = db.Column(db.Integer , ForeignKey(Product.id))
    product = db.relationship('Product', backref='order_products')
    quantity = db.Column(db.Integer)
=======
    data = db.Column(db.DateTime)

class Order_product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    order_id = db.Column(db.Integer , ForeignKey(Orders.order_id))
    produc_id = db.Column(db.Integer , ForeignKey(Product.id))
    quantity = db.Column(db.Integer)
>>>>>>> eb25130f00fbbe7d89fca4de06b8cc859f6625aa
