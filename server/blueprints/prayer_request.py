from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import PrayerRequest, db
from schemas import PrayerRequestSchema

prayer_request_bp = Blueprint('requests', __name__)

@prayer_request_bp.route('/new', methods=['POST'])
def create_request():
    data = request.get_json()
    new_request = PrayerRequest(
        request = data.get('request'),
        timestamp = data.get('timestamp')
    )

    new_request.save()

    return jsonify({"message": "Request created successfully"}), 201

@prayer_request_bp.route('/<int:request_id>', methods=['GET'])
def get_request(request_id):
    request = PrayerRequest.query.get_or_404(request_id)
    response = PrayerRequestSchema().dump(request)
    return jsonify(response), 200


@prayer_request_bp.route('/update/<int:request_id>', methods=['PUT'])
# @jwt_required()
def update_request(request_id):
    request = PrayerRequest.query.get_or_404(request_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(request, key, value)
    db.session.commit()
    return jsonify({"message": "Request updated successfully"}), 200

@prayer_request_bp.route('/delete/<int:request_id>', methods=['DELETE'])
# @jwt_required()
def delete_request(request_id):
    request = PrayerRequest.query.get_or_404(request_id)
    db.session.delete(request)
    db.session.commit()
    return jsonify({"message": "Request deleted successfully"}), 200