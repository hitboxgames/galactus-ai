import os
from flask import Flask

server = Flask(__name__)

def create_app():
    print("Creating app...")
    debug = os.environ.get("IS_DEBUG")
    server.debug = True if debug == "TRUE"  else False
    
    import app.routes
    return server