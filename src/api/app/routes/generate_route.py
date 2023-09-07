"""
generate_route.py

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
    :raises: 500 error if an error occurs
    """
    try:
        prompt = request.json["prompt"]
        buffer = mesh_service.generate_mesh_as_glb(prompt)
        return Response(
            buffer.read(),
            mimetype="model/gltf-binary",
            headers={
                "Content-Disposition": f'attachment;filename={prompt}.glb'
            },
            status=200
        )
    except Exception as error:
        return Response(
            error,
            mimetype="application/json",
            status=500
        )

@generate.route("/generate_obj", methods=["POST"])
@authentication_middleware
def generate_mesh_as_obj() -> Response:
    """
    Generate a mesh as obj from the given prompt

    :param prompt (any): The text prompt to generate a mesh from
    :return (json): response containing the generated mesh as obj
    :raises: 500 error if an error occurs
    """
    try:
        prompt = request.json["prompt"]
        buffer = mesh_service.generate_mesh_as_obj(prompt)
        return Response(
            buffer.read(),
            mimetype="model/obj",
            headers={
                "Content-Disposition": f'attachment;filename={prompt}.obj'
            },
            status=200
        )
    except Exception as error:
        return Response(
            error,
            mimetype="application/json",
            status=500
        )
