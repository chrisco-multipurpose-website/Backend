from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt, current_user
from datetime import datetime
from models import Event, db
from schemas import EventSchema

event_bp = Blueprint('events', __name__)

@event_bp.route('/new', methods=['POST'])
@jwt_required()
def create_event():
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    data = request.get_json()
    new_event = Event(
        event_img = "images/events/outreach.png",
        event_category = data.get('event_category'),
        title = data.get('title'),
        description = data.get('description'),
        theme = data.get('theme'),
        scripture = data.get('scripture'),
        location = data.get('location'),
        date = data.get('date'),
        start_time = data.get('start_time'),
        end_time = data.get('end_time'),
        event_host = data.get('event_host'),
    )

    new_event.save()

    return jsonify({"message": "Service created successfully"}), 201

@event_bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    response = EventSchema().dump(event)
    return jsonify(response), 200

@event_bp.route('/all', methods=['GET'])
@jwt_required()
def get_all_events():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    events = Event.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = EventSchema().dump(events, many=True)

    return jsonify(response), 200

@event_bp.route('/update/<int:event_id>', methods=['PUT'])
@jwt_required()
def update_event(event_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    event = Event.query.get_or_404(event_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(event, key, value)
    db.session.commit()
    return jsonify({"message": "Event updated successfully"}), 200

@event_bp.route('/delete/<int:event_id>', methods=['DELETE'])
@jwt_required()
def delete_event(event_id):
    # Check user's role
    if current_user.role not in ['superadmin', 'admin']:
        return jsonify({"message": "Unauthorized access"}), 401
    
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully"}), 200