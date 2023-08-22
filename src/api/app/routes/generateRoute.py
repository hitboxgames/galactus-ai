import torch
import io
from flask import Response, request, Blueprint
from app.interface.mesh_generator import MeshGenerator
from app.jarvis.rendering.mesh import TriMesh
from app.jarvis.util.notebooks import decode_latent_mesh


generate = Blueprint("generate", __name__)

mesh_generator = MeshGenerator()

@generate.route("/generate", methods=["POST"])
def generate_mesh() -> torch.Tensor:
    """Generate a mesh from the given prompt"""
    print("Generating mesh")
    prompt = request.json["prompt"]
    latent = mesh_generator.generate_latent(prompt)
    tri_mesh = decode_latent_mesh(mesh_generator.transmitter_model, latent).tri_mesh()
    buf = io.BytesIO()
    tri_mesh.write_obj(buf)
    buf.seek(0)
    return Response(buf, mimetype="text/plain", headers={"Content-Disposition": "attachment;filename=mesh.obj"})

@generate.route("/save", methods=["POST"])
def save_mesh() -> torch.Tensor:
    """Save the generated mesh"""
    prompt = request.json["prompt"]
    latent = mesh_generator.generate_latent(prompt)
    mesh_generator.save_single_mesh_file(latent)

    return Response("Mesh saved", mimetype="text/plain")