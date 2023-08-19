from flask import jsonify, request, Blueprint

health_check = Blueprint("health_check", __name__)

@health_check.route("/health_check", methods=["GET"])
def health_check_route() -> str:
    """Health check route"""
    return jsonify({"message": "Server is running!"}, 200)

@health_check.route("/ping", methods=["POST"])
def ping() -> str:
    """Ping route"""
    return jsonify({"message": "pong"}, 200)
