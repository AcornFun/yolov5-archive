import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA device count:", torch.cuda.device_count())
print("Current device:", torch.cuda.current_device() if torch.cuda.is_available() else "No CUDA")
print("Device name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No CUDA")