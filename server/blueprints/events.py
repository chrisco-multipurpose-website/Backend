from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime
from models import Event
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

@event_bp.get('/all')
def get_all_events():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', type=int)

    events = Event.query.paginate(
        page = page,
        per_page = per_page
    )
        
    response = EventSchema().dump(events, many=True)

    return jsonify(response), 200