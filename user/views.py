from db import db
from flask import jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from .models import User
from . import user_bp
from functools import wraps

@user_bp.route('/', methods=['GET'])
async def get_users():
    all_users = User.query.filter(User.archive == False).all()
    
    data = []
    
    for user in all_users:
        data.append(user.serialize())
    
    return jsonifyp(data), 200

@user_bp.route('/', methods=['POST'])
async def create_user():
    data = request.json
    name = data['name']
    email = data['email'].lower()
    role = data['role']
    password = data['password']
    
    check_user = User.query.filter(User.email == email).first()
    if check_user:
        return jsonify({'message':"User exists already!"}), 400
    else:
        created_user = User(
            name=name,
            email=email,
            role=role,
            password=password
        )
        db.session.add(created_user)
        db.session.commit()
        return jsonify(created_user.serialize()), 200
    

# @user_bp.route('/login', methods=['POST'])
# async def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     user = User.query.filter(User.email == email).first()
#     if user and user.password == password:
#         access_token = create_access_token(identity=email)
#         refresh_token = create_refresh_token(identity=email)
#         return jsonify({'access_token': access_token, 'refresh_token': refresh_token}), 200
#     else:
#         return jsonify({'message': 'Invalid email or password'}), 401
    
# @user_bp.route('/refresh', methods=['POST'])
# @jwt_required(refresh=True)
# async def refresh():
#     current_user = get_jwt_identity()
#     new_access_token = create_access_token(identity=current_user)
#     return jsonify({'access_token': new_access_token}), 200

# def sync_jwt_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         return jwt_required()(fn)(*args, **kwargs)
#     return wrapper

# @user_bp.route('/details', methods=['GET'])
# @sync_jwt_required
# async def get_details():
#     current_user_email = get_jwt_identity()
    
#     # Fetch the user from the database using the email
#     user = User.query.filter_by(email=current_user_email).first()
    
#     if user:
#         return jsonify(user.serialize()), 200
#     else:
#         return jsonify({'message': 'User not found'}), 404
