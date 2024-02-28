from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
from models import ProfileDetail, db
from schemas import ProfileDetailSchema

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/details', methods=['GET'])
@jwt_required()
def get_user_profile_details():
    # Check if personal details exist for the current user
    personal_details = ProfileDetail.query.filter_by(user_id=current_user.id).first()
    if personal_details:
        response = ProfileDetailSchema().dump(personal_details)
        return jsonify(response), 200
    else:
        return jsonify({"message": "Personal details not found"}), 404

@profile_bp.route('/update', methods=['POST'])
@jwt_required()
def create_or_update_user_profile_details():
    data = request.get_json()
    # Check if personal details already exist for the current user
    personal_details = ProfileDetail.query.filter_by(user_id=current_user.id).first()
    if personal_details:
        # Personal details exist, update them
        for key, value in data.items():
            setattr(personal_details, key, value)
        db.session.commit()
        return jsonify({"message": "Profile details updated successfully"}), 200
    else:
        # Personal details do not exist, create new
        new_profile = ProfileDetail(
            phone_number=data.get('phone_number'),
            address=data.get('address'),
            bio=data.get('bio'),
            profile_picture='images/users/user-profile.jpeg',
            user_id=current_user.id
        )
        new_profile.save()
        return jsonify({"message": "Profile details created successfully"}), 201

@profile_bp.route('/delete', methods=['DELETE'])
@jwt_required()
def delete_user_profile_details():
    # Check if personal details exist for the current user
    personal_details = ProfileDetail.query.filter_by(user_id=current_user.id).first()
    if personal_details:
        personal_details.delete()
        return jsonify({"message": "Profile details deleted successfully"}), 200
    else:
        return jsonify({"message": "Personal details not found"}), 404
