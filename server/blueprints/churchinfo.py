from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import ChurchInfo
from schemas import ChurchInfoSchema

churchinfo_bp = Blueprint('churchinfo', __name__)

@churchinfo_bp.post('/new')
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


@churchinfo_bp.get('all')
def get_all_info():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    info = ChurchInfo.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = ChurchInfoSchema().dump(info, many=True)

    return jsonify(response), 200