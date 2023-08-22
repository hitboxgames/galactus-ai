import torch
import os
from app.jarvis.diffusion.sample import sample_latents
from app.jarvis.util.notebooks import decode_latent_mesh
from app.jarvis.models.download import load_model, load_config
from app.jarvis.diffusion.gaussian_diffusion import diffusion_from_config

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
        self.batch_size = 1
        self.guidance_scale = 15.0
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(self.device)
        self.transmitter_model = load_model('transmitter', device=self.device)
        self.text_model = load_model('text300M', device=self.device)
        self.diffusion = diffusion_from_config(load_config('diffusion')) 
    def generate_latent(self, prompt: str):
        """
        Generates a latent vector from a prompt.

        Args:
            prompt: The prompt to generate a latent vector from.

        Returns:
            A latent vector.
        """
        print("Generating latent vector")
        latents = sample_latents(
            batch_size = self.batch_size,
            model = self.text_model,
            diffusion = self.diffusion,
            guidance_scale = self.guidance_scale,
            model_kwargs = dict(texts=[prompt] * self.batch_size),
            progress=True,
            clip_denoised=True,
            use_fp16=True,
            use_karras=True,
            karras_steps=64,
            sigma_min=1e-3,
            sigma_max=160,
            s_churn=0,
        )
        print("Generated latent vector")
        return latents

    def save_single_mesh_file(self, latent: torch.Tensor):
        """
        Saves a latent vector to a file.

        Args:
            latents: A tensor of latent vectors.
        
        Returns:
            A list of filenames.
        """
        print("Saving mesh to file")
        if not os.path.exists("output"):
            os.mkdir("output")
        
            t = decode_latent_mesh(self.transmitter_model, latent).tri_mesh()
            obj_filename = f'output/mesh.obj'
            with open(obj_filename, 'w') as f:
                t.write_obj(f)
            print("Saved mesh to file")
            return obj_filename
        
    def latent_to_obj(self, latent: torch.Tensor):
        """
        Generates a mesh from a latent vector.

        Args:
            latent: A tensor of latent vectors.

        Returns:
            The .obj format data as a string.
        """
        decoded = decode_latent_mesh(self.transmitter_model, latent).tri_mesh()
        obj_data = self.mesh_to_obj(decoded.vertices, decoded.faces)
        return obj_data
        
    def mesh_to_obj(self, vertices: torch.Tensor, faces: torch.Tensor) -> str:
        """
        Converts a mesh to the .obj format.

        Args:
            vertices: A tensor of vertices.
            faces: A tensor of faces.
        
        Returns:
            The .obj format data as a string.
        """
        obj_lines = []

        # Add vertices to the obj string
        for vertex in vertices:
            obj_lines.append(f"v {' '.join(map(str, vertex))}")

        # Add faces to the obj string
        for face in faces:
            # OBJ format uses 1-indexed vertices
            obj_lines.append(f"f {' '.join(map(lambda x: str(x+1), face))}")

        return "\n".join(obj_lines)

        
    
    

    

            