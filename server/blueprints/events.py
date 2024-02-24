from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime
from models import Event, db
from schemas import EventSchema

event_bp = Blueprint('events', __name__)

@event_bp.post('/new')
def create_event():
    data = request.get_json()
    new_event = Event(
        name= data.get('title'),
        description=data.get('description')
    )

    new_event.save()

    return jsonify({"message": "Service created successfully"}), 201

@event_bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    response = EventSchema().dump(event)
    return jsonify(response), 200

@event_bp.route('/all', methods=['GET'])
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
# @jwt_required()
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    data = request.get_json()
    for key, value in data.items():
        setattr(event, key, value)
    db.session.commit()
    return jsonify({"message": "Event updated successfully"}), 200

@event_bp.route('/delete/<int:event_id>', methods=['DELETE'])
# @jwt_required()
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Event deleted successfully"}), 200