"""
generateRoute.py

API routes for generating meshes
"""
import io
from flask import Response, request, Blueprint
from app.services.generation_service import MeshService
from app.middleware.authentication import authentication_middleware

generate = Blueprint("generate", __name__)
mesh_service = MeshService()

@generate.route("/generate_glb", methods=["POST"])
@authentication_middleware
def generate_mesh_as_glb() -> Response:
    """
    Generate a mesh as glb from the given prompt

    :param prompt (any): The text prompt to generate a mesh from
    :return (json): response containing the generated mesh as glb
    """
    prompt = request.json["prompt"]
    buffer = mesh_service.generate_mesh_as_glb(prompt)
    return Response(
        buffer,
        mimetype="text/plain",
        headers={"Content-Disposition": f'attachment;filename={prompt}.glb'}
    )

@generate.route("/generate_obj", methods=["POST"])
@authentication_middleware
def generate_mesh_as_obj() -> Response:
    """
    Generate a mesh as obj from the given prompt

    :param prompt (any): The text prompt to generate a mesh from
    :return (json): response containing the generated mesh as obj
    """
    print("Generating mesh")
    prompt = request.json["prompt"]
    buffer = mesh_service.generate_mesh_as_obj(prompt)
    return Response(
        buffer,
        mimetype="text/plain",
        headers={"Content-Disposition": f'attachment;filename={prompt}.obj'}
    )
