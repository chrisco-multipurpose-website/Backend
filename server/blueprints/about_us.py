from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt, current_user
from models import AboutUs, db
from schemas import AboutUsSchema

about_bp = Blueprint('about', __name__)

@about_bp.route('/new', methods=['POST'])
@jwt_required()
def create_about_info():
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    data = request.get_json()
    new_about_us_info = AboutUs(
        title = data.get('title'),
        description = data.get('description'),
        about_img = data.get('about_img'),
        mission = data.get('mission'),
        vision = data.get('vision'),
        faith = data.get('faith'),
        faith_img = data.get('faith_img'),
        word = data.get('word'),
        word_img = data.get('word_img'),
        trinity = data.get('trinity'),
        trinity_img = data.get('trinity_img'),
        baptism = data.get('baptism'),
        baptism_img = data.get('baptism_img'),
        church_slogan = data.get('church_slogan'),
        purpose = data.get('purpose'),
        history_desc = data.get('history_desc')
    )

    new_about_us_info.save()

    return jsonify({"message": "Aboutinfo created successfully"}), 201

@about_bp.route('/<int:about_id>', methods=['GET'])
def get_aboutinfo(about_id):
    about = AboutUs.query.get_or_404(about_id)
    response = AboutUsSchema().dump(about)
    return jsonify(response), 200

@about_bp.route('/all', methods=['GET'])
def get_all_about_us_info():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    about_info = AboutUs.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = AboutUsSchema().dump(about_info, many=True)

    return jsonify(response), 200

@about_bp.route('/update/<int:about_id>', methods=['PUT'])
@jwt_required()
def update_aboutinfo(about_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    about = AboutUs.query.get_or_404(about_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(about, key, value)
    db.session.commit()
    return jsonify({"message": "Aboutinfo updated successfully"}), 200

@about_bp.route('/delete/<int:about_id>', methods=['DELETE'])
@jwt_required()
def delete_aboutinfo(about_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    about = AboutUs.query.get_or_404(about_id)
    db.session.delete(about)
    db.session.commit()
    return jsonify({"message": "Aboutinfo deleted successfully"}), 200