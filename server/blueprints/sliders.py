from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime
from models import SliderImage
from schemas import SliderImageSchema

slider_bp = Blueprint('sliders', __name__)

@slider_bp.get('/all')
def get_all_sliders():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    sliders = SliderImage.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = SliderImageSchema().dump(sliders, many=True)

    return jsonify(response), 200