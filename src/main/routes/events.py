from flask import Blueprint, jsonify, request

events_route_bp = Blueprint('events_route', __name__)

from src.validators.events_creator_validator import events_creator_validator

from src.http_types.http_request import HttpRequest

from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

@events_route_bp.route("/event", methods=["POST"])
def create_new_event():
    events_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    eventos_repo = EventosRepository()
    events_creator = EventsCreator(eventos_repo)

    try:
        response = events_creator.create_event(http_request)
        return jsonify(response.body), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
