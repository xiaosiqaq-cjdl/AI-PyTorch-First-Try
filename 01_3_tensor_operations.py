import torch

x = torch.tensor([1.0, 2.0, 3.0])

print("x + 5 = ", x+5)
print("x * 2 = ", x * 2)
print("x ** 2 = ", x **2)

a = torch.tensor([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0]
])

b = torch.tensor([10.0, 20.0, 30.0])

print(a+b)

c = torch.tensor([
    [100.0],
    [200.0]
])

print(a+c)

print("a shape:", a.shape)
print("b shape:", b.shape)
print("c shape:", c.shape)