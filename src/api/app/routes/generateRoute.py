from flask import jsonify, request, Blueprint
from app.interface.mesh_generator import MeshGenerator
from app.interface.model_loader import ModelLoader

generate = Blueprint("generate", __name__)

model = ModelLoader()
mesh_generator = MeshGenerator(model)

@generate.route("/generate", methods=["POST"])
def generate():
    pass


        