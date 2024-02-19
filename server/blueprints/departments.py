from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from models import Department
from schemas import DepartmentSchema

department_bp = Blueprint('departments', __name__)

@department_bp.post('/new')
def create_department():
    data = request.get_json()
    new_department = Department(
        name= data.get('title'),
        description=data.get('description'),
        department_img = data.get('department_img')
    )

    new_department.save()

    return jsonify({"message": "Department created successfully"}), 201

@department_bp.get('/all')
def get_all_departments():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    departments = Department.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = DepartmentSchema().dump(departments, many=True)

    return jsonify(response), 200