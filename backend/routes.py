from flask import request,jsonify
from app import app,db
from models import*
from flask_jwt_extended import create_access_token,jwt_required,get_jwt_identity



@app.route('/signup' , methods = ['POST'])
def signup():
    data = request.get_json()
    new_user = User(username = data.get('email') , password = data.get('password') , role = 'user')
    db.session.add(new_user)
    db.session.commit()

    # access_token = create_access_token(identity=new_user.id, additional_claims={'role': 'user'})

    if data.get('role') == 'manager':
        user = User.query.filter_by(username=data['email']).first()
        new_request = Manager_request(user_id = user.id)
        db.session.add(new_request)
        db.session.commit()

    return jsonify({'message': 'Item added successfully'})

@app.route('/login' , methods = ['POST','GET'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['email']).first()
    if not user or user.password != data['password']:
       return jsonify({'message' : 'Incorrect password/user' , 'login' : False})
    # access_token = create_access_token(identity=user.id, additional_claims={'role': user.role})
    
    access_token = create_access_token(identity={'id': user.id, 'role': user.role})   
    print(access_token)
    return jsonify({'message' : 'Login successful' , 'login' : True , 'access_token' : access_token , 'role' : user.role, 'username': user.username})
        
    
@app.route('/manager_request' , methods = ['POST','GET'])
@jwt_required()
def manager_request():

    if request.method == 'GET':
  
        print('11111111111')
        current_user = get_jwt_identity()
        print(current_user)

        if current_user['role'] != 'admin': 
            print(current_user['id'])
            return jsonify({'message' : 'only admin access'})

        name = {}
        temp = db.session.query(User).join(Manager_request).filter(User.id == Manager_request.user_id).all()
        print(temp)
        for i in temp:
            name[i.id] = i.username
        return jsonify({'user': name})

    elif request.method == 'POST':

        current_user = get_jwt_identity()
        print(current_user)

        if current_user['role'] != 'admin': 
            print(current_user['id'])
            return jsonify({'message' : 'only admin access'})

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

@app.route('/edit_category' , methods = ['PATCH','GET','POST'])
def edit_cat():
    if request.method == 'GET':
        cat = []
        temp = Category.query.all()
        for i in temp:
            cat.append({'key' : i.id , 'value' : {'name' : i.name , 'desc' : i.description}})
        return jsonify({'category':cat})
    
    elif request.method == 'PATCH':
        data = request.get_json()
        print(data)
        print(data.get('id')['key'])
        cat = Category.query.get(data.get('id')['key'])
        print(cat)
        if cat:
            cat.name = data.get('name')
            cat.description = data.get('desc')
            db.session.commit()
            return jsonify({'message' : 'Category edited'})
        return jsonify({'message' : 'Category error'})
    
    elif request.method == 'POST':
        temp = request.get_json()
        print(temp)
        prod = Product.query.filter_by(cat_id=temp['cat']).all()
        print(prod)
        for i in prod:
            db.session.delete(i)
        cat = Category.query.get(temp['cid'])
        db.session.delete(cat)
        db.session.commit()
        return jsonify({'message' : 'Category deleted'})

@app.route('/create_product' , methods = ['POST','GET'])
def create_prod():
    if request.method == 'GET':
        name = []
        temp = Category.query.all()
        for i in temp:
            # name[i.id] = i.name
            name.append({'key':i.id , 'value' : i.name })
        return jsonify({'category':name})
    
    if request.method == 'POST':
        data = request.get_json()
        new_prod = Product(cat_id = data.get('cat_id'),name = data.get('name') , description = data.get('desc') , price = data.get('price'),stock = data.get('stock'))
        db.session.add(new_prod)
        db.session.commit()
        return jsonify({'message' : 'Product created'})
    


@app.route('/view_product',methods=['GET','POST'])
def view_prod():
    product = {}
    temp = db.session.query(Product)
    for i in temp:
        product[i.id] = i.name

    return jsonify({'product': product})


@app.route('/delete_product',methods=['POST','GET'])
def delete_prod():
    data = request.get_json()
    p_id = data['pid']
    prod = Product.query.get(p_id)
    print(prod)
    db.session.delete(prod)
    db.session.commit()
    return jsonify({'message' : 'Product deleted'})

@app.route('/view_category',methods=['GET','POST'])
def view_cat():
    category = {}
    temp = db.session.query(Category)
    for i in temp:
        category[i.id] = i.name

    return jsonify({'category': category})

@app.route('/delete_category',methods=['GET','POST'])
def delete_category():
    products = []
    temp = request.get_json()
    print(temp)
    prod = Product.query.filter_by(cat_id=temp['cat']).all()
    print(prod)
    for i in prod:
        db.session.delete(i)
    cat = Category.query.get(temp['cid'])
    db.session.delete(cat)
    db.session.commit()
    return jsonify({'message' : 'Category deleted'})