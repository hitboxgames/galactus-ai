import torch
from app.jarvis.diffusion.sample import sample_latents
from app.jarvis.util.notebooks import decode_latent_images

class MeshGenerator:
    """
    Class that generates meshes from a prompt.

    Attributes:
        model_loader: A ModelLoader object.
        batch_size: The batch size to use when generating a latent vector.
        guidance_scale: The guidance scale to use when generating a latent vector.
    """
    def __init__(self, model_loader):
        self.model_loader = model_loader
        self.batch_size = 1
        self.guidance_scale = 15.0
    
    def generate_latent(self, prompt: str):
        """
        Generates a latent vector from a prompt.

        Args:
            prompt: The prompt to generate a latent vector from.

        Returns:
            A latent vector.
        """
        latents = sample_latents(
            batch_size = self.batch_size,
            model = self.model_loader.text_model,
            diffusion = self.model_loader.diffusion,
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
        return latents

    def save_latents_to_files(self, latents: torch.Tensor):
        """
        Saves a latent vector to a file.

        Args:
            latents: A tensor of latent vectors.
        
        Returns:
            A list of filenames.
        """
        filenames = []
        for i, latent in enumerate(latents):
            t = decode_latent_images(
                self.model_loader.transmitter_model, latent
            ).tri_mesh()
            
            filename = f'example_mesh_{i}.obj'
            with open(filename, 'w') as f:
                t.write_obj(f)
            filenames.append(filename)
        return filenames
  