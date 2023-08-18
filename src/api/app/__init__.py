import os
from flask import Flask

server = Flask(__name__)

def create_app():
    """
    This function is used to create the Flask app.

    Returns:
        Flask: The flask app with all routes attached.
    """
    debug = os.environ.get("IS_DEBUG")
    server.debug = True if debug == "TRUE"  else False
    
    import app.routes

    return server