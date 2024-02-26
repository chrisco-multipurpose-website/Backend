from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import ChurchInfo, db
from schemas import ChurchInfoSchema

churchinfo_bp = Blueprint('churchinfo', __name__)

@churchinfo_bp.route('/new', methods=['POST'])
def create_info():
    data = request.get_json()
    new_info = ChurchInfo(
        contact= data.get('contact'),
        location=data.get('location'),
        facebook=data.get('facebook'),
        instagram=data.get('instagram'),
        youtube=data.get('youtube'),
        tiktok=data.get('tiktok'),
        x_social=data.get('x_social')
    )

    new_info.save()

    return jsonify({"message": "Info created successfully"}), 201


@churchinfo_bp.route('/<int:churchinfo_id>', methods=['GET'])
def get_info(event_id):
    event = ChurchInfo.query.get_or_404(event_id)
    response = ChurchInfoSchema().dump(event)
    return jsonify(response), 200

@churchinfo_bp.route('all', methods=['GET'])
def get_all_info():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    info = ChurchInfo.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = ChurchInfoSchema().dump(info, many=True)

    return jsonify(response), 200

@churchinfo_bp.route('/update/<int:churchinfo_id>', methods=['PUT'])
# @jwt_required()
def update_event(churchinfo_id):
    info = ChurchInfo.query.get_or_404(churchinfo_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(info, key, value)
    db.session.commit()
    return jsonify({"message": "Info updated successfully"}), 200

@churchinfo_bp.route('/delete/<int:churchinfo_id>', methods=['DELETE'])
# @jwt_required()
def delete_event(churchinfo_id):
    info = ChurchInfo.query.get_or_404(churchinfo_id)
    db.session.delete(info)
    db.session.commit()
    return jsonify({"message": "Info deleted successfully"}), 200