from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import ProfileDetail, db
from schemas import ProfileDetailSchema

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/new', methods=['POST'])
def create_userprofile():
    data = request.get_json()
    new_profile = ProfileDetail(
        phone_number = data.get('phone_number'),
        address = data.get('address'),
        bio = data.get('bio'),
        profile_picture = data.get('profile_picture')
    )

    new_profile.save()

    return jsonify({"message": "Profile created successfully"}), 201

@profile_bp.route('/<int:profile_id>', methods=['GET'])
def get_department(profile_id):
    profile = ProfileDetail.query.get_or_404(profile_id)
    response = ProfileDetailSchema().dump(profile)
    return jsonify(response), 200


@profile_bp.route('/update/<int:profile_id>', methods=['PUT'])
# @jwt_required()
def update_department(profile_id):
    profile = ProfileDetail.query.get_or_404(profile_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(profile, key, value)
    db.session.commit()
    return jsonify({"message": "Profile updated successfully"}), 200

@profile_bp.route('/delete/<int:profile_id>', methods=['DELETE'])
# @jwt_required()
def delete_department(profile_id):
    profile = ProfileDetail.query.get_or_404(profile_id)
    db.session.delete(profile)
    db.session.commit()
    return jsonify({"message": "Profile deleted successfully"}), 200