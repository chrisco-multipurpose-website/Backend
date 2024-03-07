from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt, current_user
from datetime import datetime
from models import Service, db
from schemas import ServiceSchema

service_bp = Blueprint('services', __name__)

@service_bp.route('/new', methods=['POST'])
@jwt_required()
def create_service():
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    data = request.get_json()
    new_service = Service(
        name= data.get('name'),
        start_time=data.get('start_time'),
        end_time=data.get('end_time'),
        service_type=data.get('service_type')
    )

    new_service.save()

    return jsonify({"message": "Service created successfully"}), 201

@service_bp.route('/all', methods=['GET'])
def get_all_services():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    services = Service.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = ServiceSchema().dump(services, many=True)

    return jsonify(response), 200

@service_bp.route('/update/<int:service_id>', methods=['PATCH'])
@jwt_required()
def update_service(service_id):
     # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    service = Service.query_or_404(service_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(service, key, value)
    db.session.commit()
    return jsonify({"message": "Service updated successfully"}), 200


@service_bp.route('/delete/<int:service_id>', methods=['DELETE'])
@jwt_required()
def delete_service(service_id):
     # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    service = Service.query_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully"}), 201