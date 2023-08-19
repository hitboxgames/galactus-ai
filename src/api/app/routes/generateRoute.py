import torch
from flask import Response, request, Blueprint
from app.interface.mesh_generator import MeshGenerator
from app.interface.model_loader import ModelLoader
from app.jarvis.util.notebooks import decode_latent_mesh
from app.jarvis.rendering.mesh import TriMesh

generate = Blueprint("generate", __name__)

model = ModelLoader()
mesh_generator = MeshGenerator(model)

@generate.route("/generate", methods=["POST"])
def generate_mesh() -> torch.Tensor:
    """Generate a mesh from the given prompt"""
    print("Generating mesh")
    prompt = request.json["prompt"]
    latent = mesh_generator.generate_latent(prompt)
    obj = mesh_generator.latent_to_obj(latent)

    return Response(obj, mimetype="text/plain")
