from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt, current_user
from models import Department, db
from schemas import DepartmentSchema

department_bp = Blueprint('departments', __name__)

@department_bp.route('/new', methods=['POST'])
@jwt_required()
def create_department():
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    data = request.get_json()
    new_department = Department(
        name= data.get('title'),
        description=data.get('description'),
        department_img = "images/departments/development.png"
    )

    new_department.save()

    return jsonify({"message": "Department created successfully"}), 201

@department_bp.route('/<int:department_id>', methods=['GET'])
def get_department(department_id):
    department = Department.query.get_or_404(department_id)
    response = DepartmentSchema().dump(department)
    return jsonify(response), 200

@department_bp.route('/all', methods=['GET'])
def get_all_departments():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    departments = Department.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = DepartmentSchema().dump(departments, many=True)

    return jsonify(response), 200

@department_bp.route('/update/<int:department_id>', methods=['PUT'])
@jwt_required()
def update_department(department_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    department = Department.query.get_or_404(department_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(department, key, value)
    db.session.commit()
    return jsonify({"message": "Department updated successfully"}), 200

@department_bp.route('/delete/<int:department_id>', methods=['DELETE'])
@jwt_required()
def delete_department(department_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()
    return jsonify({"message": "Department deleted successfully"}), 200