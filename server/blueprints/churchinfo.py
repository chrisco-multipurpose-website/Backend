from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt, current_user
from models import ChurchInfo, db
from schemas import ChurchInfoSchema

churchinfo_bp = Blueprint('churchinfo', __name__)

@churchinfo_bp.route('/new', methods=['POST'])
@jwt_required()
def create_info():
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    data = request.get_json()
    new_info = ChurchInfo(
        contact = data.get('contact'),
        location = data.get('location'),
        address = data.get('address'),
        email = data.get('email'),
        website = data.get('website'),
        facebook_url = data.get('facebook'),
        instagram_url = data.get('instagram'),
        youtube_url = data.get('youtube'),
        tiktok_url = data.get('tiktok'),
        x_url = data.get('x_social')
    )

    new_info.save()

    return jsonify({"message": "Info created successfully"}), 201


@churchinfo_bp.route('/<int:churchinfo_id>', methods=['GET'])
def get_info(churchinfo_id):
    info = ChurchInfo.query.get_or_404(churchinfo_id)
    response = ChurchInfoSchema().dump(info)
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
@jwt_required()
def update_info(churchinfo_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    info = ChurchInfo.query.get_or_404(churchinfo_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(info, key, value)
    db.session.commit()
    return jsonify({"message": "Info updated successfully"}), 200

@churchinfo_bp.route('/delete/<int:churchinfo_id>', methods=['DELETE'])
@jwt_required()
def delete_event(churchinfo_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    info = ChurchInfo.query.get_or_404(churchinfo_id)
    db.session.delete(info)
    db.session.commit()
    return jsonify({"message": "Info deleted successfully"}), 200