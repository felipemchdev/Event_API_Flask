from flask import Blueprint, jsonify, request

subscribers_route_bp = Blueprint('subscribers_route', __name__)

from src.validators.subscribers_creator_validator import subscribers_creator_validator
from src.http_types.http_request import HttpRequest
from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.model.repositories.subscribers_repository import SubscribersRepository

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
        return jsonify({"error": str(e)}), 500
