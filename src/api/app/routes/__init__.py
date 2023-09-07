from app import server
from .generate_route import generate
from ..routes.healthCheck import health_check

print("Registering blueprints...")

server.register_blueprint(generate, url_prefix="/")
server.register_blueprint(health_check, url_prefix="/")