"""
model_loader.py

In order for the mesh generator to work we need to load all the models and configurations needed.
We will use the jarvis library to load the models and configurations.
Then we will initialize the ModelLoader class which will load all the models and 
configurations in our mesh_generator.py file.
"""
import torch
from app.jarvis.models.download import load_model, load_config
from app.jarvis.diffusion.gaussian_diffusion import diffusion_from_config

class ModelLoader:
    """
    This class loads all models and configurations needed for the mesh generator.
    :return: ModelLoader
    """
    def __init__(self):
        """
        The constructor for the ModelLoader class.

        :param device: Which device to run the model on, will default to cuda if 
                       available otherwise cpu.
        :param transmitter_model: The transmitter model provided by the jarvis library.
        :param text_model: The text model provided by the jarvis library.
        :param diffusion: The diffusion model provided by the jarvis library.
        """
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.transmitter_model = load_model('transmitter', device=self.device)
        self.text_model = load_model('text300M', device=self.device)
        self.diffusion = diffusion_from_config(load_config('diffusion'))
