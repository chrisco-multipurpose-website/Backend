from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import AboutUs
from schemas import AboutUsSChema

about_bp = Blueprint('about', __name__)

@about_bp.post('/new')
def create_about_info():
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

    return jsonify({"message": "About created successfully"}), 201

@about_bp.get('/all')
def get_all_about_us_info():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    about_info = AboutUs.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = AboutUsSChema().dump(about_info, many=True)

    return jsonify(response), 200