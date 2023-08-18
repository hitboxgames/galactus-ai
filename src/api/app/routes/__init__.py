from app import server
from ..routes.generateRoute import generate

server.register_blueprint(generate, url_prefix="/")