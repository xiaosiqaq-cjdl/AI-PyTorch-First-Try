import torch

x = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

print("x:")
print(x)
print("shape:", x.shape)

y = x.reshape(3,2)

print("y:")
print(y)
print("shape:", y.shape)

z = x.reshape(-1)
print("z:")
print(z)
print(z.shape)

a = torch.tensor([1.0, 2.0, 3.0])

print(a.shape)

b = a.unsqueeze(0)
print("b is")
print(b)
print(b.shape)

c = a.unsqueeze(1)

x = torch.tensor([[1.0, 2.0, 3.0]])

print(x.shape)

y = x.squeeze()

print(y)
print(y.shape)