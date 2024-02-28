from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
from models import PrayerRequest, db
from schemas import PrayerRequestSchema

prayer_request_bp = Blueprint('requests', __name__)

@prayer_request_bp.route('/all', methods=['GET'])
@jwt_required()
def get_user_prayer_requests():
    user_requests = PrayerRequest.query.filter_by(user_id=current_user.id).all()
    response = PrayerRequestSchema().dump(user_requests, many=True)
    return jsonify(response), 200

@prayer_request_bp.route('/new', methods=['POST'])
@jwt_required()
def create_prayer_request():
    data = request.get_json()
    new_request = PrayerRequest(
        request=data.get('request'),
        user_id=current_user.id
    )
    new_request.save()
    return jsonify({"message": "Prayer request created successfully"}), 201

@prayer_request_bp.route('/<int:request_id>', methods=['GET'])
@jwt_required()
def get_prayer_request(request_id):
    request = PrayerRequest.query.get_or_404(request_id)
    if request.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403
    response = PrayerRequestSchema().dump(request)
    return jsonify(response), 200

@prayer_request_bp.route('/update/<int:request_id>', methods=['PUT'])
@jwt_required()
def update_prayer_request(request_id):
    request = PrayerRequest.query.get_or_404(request_id)
    if request.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403
    data = request.get_json()
    for key, value in data.items():
        setattr(request, key, value)
    db.session.commit()
    return jsonify({"message": "Prayer request updated successfully"}), 200

@prayer_request_bp.route('/delete/<int:request_id>', methods=['DELETE'])
@jwt_required()
def delete_prayer_request(request_id):
    request = PrayerRequest.query.get_or_404(request_id)
    if request.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403
    db.session.delete(request)
    db.session.commit()
    return jsonify({"message": "Prayer request deleted successfully"}), 200
