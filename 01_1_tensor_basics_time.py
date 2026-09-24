import time

start = time.time()

import torch

print("Import torch:", time.time() - start)

start = time.time()

x = torch.tensor([1.0, 2.0, 3.0])

print(x)
print(x.shape)
print(x.dtype)

print("Tensor operations:", time.time() - start)