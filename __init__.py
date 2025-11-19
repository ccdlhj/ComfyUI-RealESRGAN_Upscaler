'''RealEsrganUpscaler __init__ file.'''
import sys

try:
    from torchvision.transforms.functional_tensor import rgb_to_grayscale
except ImportError:
    from torchvision.transforms.functional import rgb_to_grayscale


    class _FunctionalTensorShim:
        rgb_to_grayscale = rgb_to_grayscale


    sys.modules["torchvision.transforms.functional_tensor"] = _FunctionalTensorShim()
# Import the Python modules.
from .realesrgan.realesrgan_upscaler import *
from .realesrgan.show_data import *

NODE_CLASS_MAPPINGS = {
    "🚀 Universal RealESRGAN Upscaler": RealEsrganUpscaler,
    "🧳 Show Data": ShowData,
}

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

# Print message into the terminal window.
print("\033[34mComfyUI RealEsrganUpscaler Nodes: \033[92mLoaded\033[0m")
