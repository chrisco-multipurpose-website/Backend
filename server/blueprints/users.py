from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import User, db
from schemas import UserSchema

user_bp = Blueprint('users', __name__)

@user_bp.route('/<int:user_id>', methods=['GET'])
# @jwt_required()
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    response = UserSchema().dump(user)
    return jsonify(response), 200

@user_bp.route('/all', methods=['GET'])
# @jwt_required()
def get_all_users():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    users = User.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = UserSchema().dump(users, many=True)

    return jsonify(response), 200


@user_bp.route('/update/<int:user_id>', methods=['PUT'])
# @jwt_required()
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200

@user_bp.route('/delete/<int:user_id>', methods=['DELETE'])
# @jwt_required()
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200