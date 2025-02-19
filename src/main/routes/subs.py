from flask import Blueprint, jsonify, request

subscribers_route_bp = Blueprint('subscribers_route', __name__)

from src.http_types import http_response
from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.http_types.http_request import HttpRequest
from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

from src.controllers.subscribers.subscribers_manager import SubscribersManager

@subscribers_route_bp.route("/subscriber", methods=["POST"])
def create_new_subscriber():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    subscribers_repo = SubscribersRepository()
    subscribers_creator = SubscribersCreator(subscribers_repo)

    try:
        response = subscribers_creator.create_subscriber(http_request)
        return jsonify(response.body), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@subscribers_route_bp.route("/subscriber/event/<event_id>", methods=["GET"])
@subscribers_route_bp.route("/subscriber/link/<link>/event/<event_id>", methods=["GET"])
def subscribers_by_link(event_id, link=None):
    http_request = HttpRequest(body={}, params={"event_id": event_id, "link": link})

    subscribers_repo = SubscribersRepository()
    subscribers_manager = SubscribersManager(subscribers_repo)

    http_response = subscribers_manager.get_subscribers_by_link(http_request)

    return jsonify(http_response.body), http_response.status_code

@subscribers_route_bp.route("/subscriber/ranking/event/<event_id>", methods=["GET"])
def event_ranking(event_id):
    http_request = HttpRequest(body={}, params={"event_id": event_id})

    subscribers_repo = SubscribersRepository()
    subscribers_manager = SubscribersManager(subscribers_repo)

    http_response = subscribers_manager.get_event_ranking(http_request)

    return jsonify(http_response.body), http_response.status_code