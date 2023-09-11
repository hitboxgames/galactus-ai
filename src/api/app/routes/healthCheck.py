from flask import jsonify, Blueprint
from app.middleware.authentication import authentication_middleware

health_check = Blueprint("health_check", __name__)

@health_check.route("/health_check", methods=["GET"])
@authentication_middleware
def health_check_route() -> str:
    """Health check route"""
    return jsonify({"message": "Server is running!"}, 200)

@health_check.route("/ping", methods=["POST"])
@authentication_middleware
def ping() -> str:
    """Ping route"""
    return jsonify({"message": "pong"}, 200)

@health_check.route("/", methods=["GET"])
def home() -> str:
    """Home route"""
    return jsonify({"message": "Welcome to the API!"}, 200)
