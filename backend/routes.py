from flask import request,jsonify
from app import app

@app.route('/login_new')
def login():
    data = request.get_json()
    print(data['name'])
    return jsonify({'message': 'Item added successfully'})

