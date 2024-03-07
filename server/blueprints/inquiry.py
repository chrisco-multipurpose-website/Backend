from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
from models import Inquiry, db
from schemas import InquirySchema

inquiry_bp = Blueprint('inquiries', __name__)

@inquiry_bp.route('/create', methods=['POST'])
def create_inquiry():
    # Parse request data
    data = request.get_json()

    # Validate request data
    if 'name' not in data or 'email' not in data or 'inquiry' not in data:
        return jsonify({'message': 'Name, email, and inquiry are required'}), 400

    # Create a new inquiry
    new_inquiry = Inquiry(
        name=data.get('name'),
        email=data.get('email'),
        inquiry=data.get('inquiry')
    )

    # Add the inquiry to the database
    new_inquiry.save()

    return jsonify({'message': 'Inquiry created successfully'}), 201

@inquiry_bp.route('/all', methods=['GET'])
@jwt_required()  # Requires JWT token for authentication
def get_all_inquiries():
    # Check if current user is superadmin or admin
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({'message': 'Unauthorized access'}), 401  # Forbidden

    # Get pagination parameters from request query
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    # Query inquiries with pagination
    inquiries = Inquiry.query.paginate(
        page=page,
        per_page=per_page,
        # error_out=False  # Do not throw error if page is out of range
    )
    response = InquirySchema().dump(inquiries, many=True)

    return jsonify(response), 200

@inquiry_bp.route('/delete/<int:inquiry_id>', methods=['DELETE'])
@jwt_required()  # Requires JWT token for authentication
def delete_inquiry(inquiry_id):
    # Check if current user is superadmin or admin
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({'message': 'Unauthorized access'}), 401
    
    inquiry = Inquiry.query.get_or_404(inquiry_id)
    db.session.delete(inquiry)
    db.session.commit()

    return jsonify({'message': 'Inquiry deleted successfully'}), 200