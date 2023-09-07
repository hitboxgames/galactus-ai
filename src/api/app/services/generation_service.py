"""
generation_service.py

This service layer is responsible for validating the prompt
and calling our meshAPI and returning a mesh.
"""
import io
from typing import Tuple, Any
from app.generator.mesh_generator import MeshGenerator
from app.jarvis.util.notebooks import decode_latent_mesh
from app.models.error_messages import (
    SUCCESSFUL_GENERATION,
    FAILED_GENERATION,
    PROMPT_LENGTH_ERROR,
    PROMPT_TYPE_ERROR
)
from app.utils.logging import CustomLogger

log = CustomLogger("MeshService")

class MeshService:
    """
    This class will validate the prompt and call the meshAPI
    to generate a mesh from the prompt.
    """
    def __init__(self):
        self.mesh_generator = MeshGenerator()
        
    @staticmethod
    def validate_prompt(prompt: Any) -> None:
        """
        We need to validate the prompt 
        before we can generate a mesh from it.

        :param prompt (any): The text prompt to validate
        :raises TypeError: If the prompt is not a string
        :raises ValueError: If the prompt is longer than 50 characters
        """
        if not isinstance(prompt, str):
            log.error(
                FAILED_GENERATION, "validate_prompt", PROMPT_TYPE_ERROR
            )
            raise TypeError(PROMPT_TYPE_ERROR)

        if len(prompt) > 50:
            log.error(
                FAILED_GENERATION, "validate_prompt", PROMPT_LENGTH_ERROR
            )
            raise ValueError(PROMPT_LENGTH_ERROR)

    @staticmethod
    def generate_mesh_as_glb(prompt: str) -> io.BytesIO:
        """
        After validation we can call the 
        meshAPI to generate our mesh.

        :param prompt (str): The text prompt to generate a mesh from
        :return: A tuple containing the mesh and the filename
        """
        try:
            MeshService.validate_prompt(prompt)

            mesh = mesh_generator.generate_latent(prompt)
            decoded_mesh = decode_latent_mesh(
                mesh_generator.model.transmitter_model,
                mesh
            ).tri_mesh()
            buffer = io.BytesIO()
            decoded_mesh.write_glb(buffer)
            buffer.seek(0)
            log.info(
                f'{SUCCESSFUL_GENERATION}: {prompt}', "generate_mesh_as_glb"
            )
            return buffer

        except Exception as error:
            log.error(
                f'{FAILED_GENERATION}: {prompt}', "generate_mesh_as_glb", error
            )
            raise error

    @staticmethod
    def generate_mesh_as_obj(prompt: str) -> Tuple[io.BytesIO, str]:
        """
        After validation we can call the 
        meshAPI to generate our mesh.

        :param prompt (str): The text prompt to generate a mesh from
        :return: A tuple containing the mesh and the filename
        """
        try:
            MeshService.validate_prompt(prompt)

            mesh = mesh_generator.generate_latent(prompt)
            decoded_mesh = decode_latent_mesh(
                mesh_generator.model.transmitter_model, 
                mesh
            ).tri_mesh()
            buffer = io.BytesIO()
            decoded_mesh.write_obj(buffer)
            buffer.seek(0)
            log.info(
                f'{SUCCESSFUL_GENERATION}: {prompt}', "generate_mesh_as_obj"
            )
            return buffer

        except Exception as error:
            log.error(
                f'{FAILED_GENERATION}: {prompt}', "generate_mesh_as_obj", error
            )
            raise error
