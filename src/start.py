import os
import traceback

from flask import Flask, jsonify, request
from unet_info import UnetInferrer

app = Flask(__name__)

APP_ROOT = os.getenv('APP_ROOT', '/app')
HOST = "0.0.0.0"
PORT_NUMBER = int(os.getenv('PORT_NUMBER', 8080))

u_net = UnetInferrer()

@app.route(APP_ROOT, method=["POST"])
def create():
    data = request.json
    prompt = data['prompt']
    return u_net.infer(prompt)