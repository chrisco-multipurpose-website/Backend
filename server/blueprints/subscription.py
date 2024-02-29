from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
from models import Subscription, db
from schemas import SubcriptionSchema

subscription_bp = Blueprint('subscriptions', __name__)

@subscription_bp.route('/create', methods=['POST'])
def create_subscription():
    data = request.get_json()

    # Validate request data
    if 'email' not in data:
        return jsonify({'message': 'Email is required'}), 400

    # Create a new subscription
    new_subscription = Subscription(email=data.get('email'))

    # Add the subscription to the database
    new_subscription.save()
    return jsonify({"message": "Subcribed successfully"})

@subscription_bp.route('/all', methods=['GET'])
@jwt_required()  # Requires JWT token for authentication
def get_subscriptions():
    # Check if current user is superadmin or admin
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({'message': 'Unauthorized access'}), 403  # Forbidden

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    # Query subscriptions with pagination
    subscriptions = Subscription.query.paginate(
        page=page,
        per_page=per_page,
        # error_out=False  # Do not throw error if page is out of range
    )

    response = SubcriptionSchema().dump(subscriptions, many=True)

    return jsonify(response), 200

@subscription_bp.route('/delete/<int:subscription_id>', methods=['DELETE'])
@jwt_required()  # Requires JWT token for authentication
def delete_subscription(subcription_id):
    # Check if current user is superadmin or admin
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({'message': 'Unauthorized access'}), 401
    
    subcription = Subscription.query.get_or_404(subcription_id)
    db.session.delete(subcription)
    db.session.commit()

    return jsonify({'message': 'Subscription deleted successfully'}), 200