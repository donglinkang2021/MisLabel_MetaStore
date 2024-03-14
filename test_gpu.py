import torch
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")
print(torch.__version__)
for i in range(torch.cuda.device_count()):
    print(f"Device {i}: {torch.cuda.get_device_name(i)}")

"""output
(meta-store) chai03% python test_gpu.py 
CUDA available: True
2.2.1+cu121
Device 0: NVIDIA GeForce RTX 4090
Device 1: NVIDIA GeForce RTX 4090
"""