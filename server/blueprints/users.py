from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity, current_user
from models import User, db
from schemas import UserSchema

user_bp = Blueprint('users', __name__)

@user_bp.route('/new', methods=['POST'])
@jwt_required()
def create_user():
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    data = request.get_json()
    
    # Determine the role for the new user based on the current user's role
    if current_user.role == 'superadmin':
        # If current user is superadmin, allow specifying the role in the request data
        role = data.get('role', 'member')  # Use 'member' as default role if not provided
    else:
        # If current user is admin, set the role as 'member' by default
        role = 'member'

    new_user = User(
        firstname=data.get('firstname'),
        lastname=data.get('lastname'),
        email=data.get('email'), 
        role=role
    )
    new_user.set_password(password='user123')
    
    new_user.save()

    return jsonify({"message": "User created successfully"}), 201


@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    response = UserSchema().dump(user)
    return jsonify(response), 200

@user_bp.route('/all', methods=['GET'])
@jwt_required()
def get_all_users():
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    users = User.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = UserSchema().dump(users, many=True)

    return jsonify(response), 200


@user_bp.route('/update/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    # Check user's role
    if current_user.role != 'superadmin':
        return jsonify({"message": "Unauthorized access"}), 401
    
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200

@user_bp.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    # Check user's role
    if current_user.role != 'superadmin':
        return jsonify({"message": "Unauthorized access"}), 401
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200