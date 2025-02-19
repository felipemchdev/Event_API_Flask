from flask import Blueprint, jsonify, request

events_link_route_bp = Blueprint('events_link_route', __name__)

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.validators.events_link_creator_validator import events_link_creator_validator
from src.controllers.events_link.events_link_creator import EventsLinkCreator
from src.model.repositories.eventos_link_repository import EventosLinkRepository

@events_link_route_bp.route("/event_link", methods=["POST"])
def create_event_link():
    events_link_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    events_link_repo = EventosLinkRepository()
    events_link_creator = EventsLinkCreator(events_link_repo)

    try:
        response = events_link_creator.create_event_link(http_request)
        return jsonify(response.body), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
