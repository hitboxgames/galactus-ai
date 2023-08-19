import torch
from app.jarvis.models.download import load_model, load_config
from app.jarvis.diffusion.gaussian_diffusion import diffusion_from_config

class ModelLoader:
    """
    Class that loads all configurations for the model.
    """
    def __init__(self):
        """
        Loads all configurations for the model.

        Attributes:
            device: The device to use.
            transmitter_model: The transmitter model.
            text_model: The text model.
            diffusion: The diffusion model.
        """
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.transmitter_model = load_model('transmitter', device=self.device)
        self.text_model = load_model('text300M', device=self.device)
        self.diffusion = diffusion_from_config(load_config('diffusion'))