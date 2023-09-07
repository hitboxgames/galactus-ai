"""
mesh_generator.py

This file contains the MeshGenerator class which is 
responsible for generating meshes from a prompt.
"""

import torch
from app.utils.logging import CustomLogger
from app.generator.loader import ModelLoader
from app.jarvis.diffusion.sample import sample_latents

class MeshGenerator:
    """
    Class that generates meshes from a prompt.

    Attributes:
        batch_size: The number of meshes to generate.
        guidance_scale: The scale of the guidance.
        device: The device to run the model on.
        transmitter_model: The transmitter model.
        text_model: The text model.
        diffusion: The diffusion model.
    """
    def __init__(self):
        """
        The constructor for the MeshGenerator class.

        :param batch_size: The number of meshes to generate.
        :param guidance_scale: The scale of the guidance.
        """
        self.batch_size = 1
        self.guidance_scale = 15.0
        self.model = ModelLoader()
    def generate_latent(self, prompt: str):
        """
        Generate a latent from a prompt.

        :param prompt (str): The text prompt to generate a latent from
        :return: The generated latent.
        """
        try:
            latents = sample_latents(
                batch_size = self.batch_size,
                model = self.model.text_model,
                diffusion = self.model.diffusion,
                guidance_scale = self.guidance_scale,
                model_kwargs = dict(texts=[prompt] * self.batch_size),
                progress=False,
                clip_denoised=True,
                use_fp16=True,
                use_karras=True,
                karras_steps=64,
                sigma_min=1e-3,
                sigma_max=160,
                s_churn=0,
            )
            return latents
        except Exception as error:
            raise error
