from flask import request,jsonify
from app import app,db
from models import*

@app.route('/signup' , methods = ['POST'])
def signup():
    data = request.get_json()
    print(data.get('email'))
    print(data.get('password'))
    print(data.get('role'))

    new_user = User(email = data.get('email') , password = data.get('password') , role = 'user')
    db.session.add(new_user)
    db.session.commit()

    if data.get('role') == 'manager':
        user = User.query.filter_by(email=data['email']).first()
        new_request = Manager_request(user_id = user.id)
        db.session.add(new_request)
        db.session.commit()
    return jsonify({'message': 'Item added successfully'})

@app.route('/login' , methods = ['POST','GET'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user.password == data['password']:
        return jsonify({'message' : 'Login successful' , 'login' : True })
    else:
        return jsonify({'message' : 'Incorrect password/user' , 'login' : False})
    
@app.route('/manager_request' , methods = ['POST','GET'])
def manager_request():
    if request.method == 'GET':
        name = {}
        temp = db.session.query(User).join(Manager_request).filter(User.id == Manager_request.user_id).all()
        print(temp)

        for i in temp:
            name[i.id] = i.email

        return jsonify({'user': name})

    elif request.method == 'POST':
        data = request.get_json()
        Manager_request.query.filter(Manager_request.user_id == data['key']).delete()
        temp = User.query.filter(User.id == data['key']).first()
        temp.role = 'manager'
        db.session.commit()
        return jsonify({'message' : 'changed role'})

@app.route('/create_category',methods = ['POST','GET'])
def create_cat():
    data = request.get_json()
    new_cat = Category(name = data.get('name') , description = data.get('desc') )
    db.session.add(new_cat)
    db.session.commit()
    return jsonify({'message' : 'Category created'})


@app.route('/create_product' , methods = ['POST','GET'])
def create_prod():
    if request.method == 'GET':
        name = {}
        temp = Category.query.all()
        for i in temp:
            name[i.id] = i.name
        return jsonify({'category':'category list'})
    
    if request.method == 'POST':
        data = request.get_json()
        new_prod = Product(cat_id = data.get('cat_id'),name = data.get('name') , description = data.get('desc') , price = data.get('price'),stock = data.get('stock'))
        db.session.add(new_prod)
        db.session.commit()
        return jsonify({'message' : 'Product created'})
