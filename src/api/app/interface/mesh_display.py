import torch
from jarvis.util.notebooks import create_pan_cameras, decode_latent_images, gif_widget

class Display:
    """
    Displays meshes.
    """
    def __init__(self, model_loader):
      """
      Args:
        model_loader: A ModelLoader object.

      """
      self.model_loader = model_loader
      self.render_mode = 'nerf'
      self.size = 64
    
    def display_latents(self, latents: torch.Tensor):
        cameras = create_pan_cameras(self.size, self.model_loader.device)

        for i, latent in enumerate(latents):
            images = decode_latent_images(
                self.model_loader.transmitter_model, 
                latent, 
                cameras, 
                render_mode=self.render_mode
          )
          display(gif_widget(images)) #BUG: display is not defined  # noqa: F821