from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime
from models import Service
from schemas import ServiceSchema

service_bp = Blueprint('services', __name__)


# def convert_time(time_str):
#     return datetime.strptime(time_str, "%I:%M %p").time()



@service_bp.post('/new')
def create_service():
    data = request.get_json()
    new_service = Service(
        name= data.get('name'),
        start_time=data.get('start_time'),
        end_time=data.get('end_time'),
        service_type=data.get('service_type')
    )

    new_service.save()

    return jsonify({"message": "Service created successfully"}), 201

@service_bp.get('/all')
def get_all_services():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    services = Service.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = ServiceSchema().dump(services, many=True)

    return jsonify(response), 200

@service_bp.put('/serviceid/<int:id>')
def update_service(id):
    service_ = Service.get_service_by_id(id=id)
    data = request.get_json()


@service_bp.delete('/serviceid/<int:id>')
def delete_service(id):
    service = Service.get_service_by_id(id=id)
    service.delete()

    return jsonify({"message": "Service deleted successfully"}), 201