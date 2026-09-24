import torch

# 0D
a = torch.tensor(5.0)
# 1D
b = torch.tensor([1.0, 2.0, 3.0])
# 2D
c = torch.tensor([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])

print("a:", a)
print("a shape:", a.shape)
print("a dim:", a.dim())

print()

print("b:", b)
print("b shape:", b.shape)
print("b dim:", b.dim())

print()

print("c:", c)
print("c shape:", c.shape)
print("c dim:", c.dim())

d = torch.tensor([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("d shape:", d.shape)
print("d dim:", d.dim())

print("70:", d[1, 2])
print("second row:", d[1])
print("second column:", d[:, 1])
print("middle block:", d[:, 1:3])