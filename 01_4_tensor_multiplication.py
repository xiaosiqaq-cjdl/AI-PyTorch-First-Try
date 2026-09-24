import torch

a = torch.tensor([
    [1.0, 2.0],[3.0, 4.0]
])

b = torch.tensor([
    [10.0, 20.0],
    [30.0, 40.0]
])

print("a*b:", a * b)

print()

print("a@b:", a @ b)
print("b@a:", b @ a)