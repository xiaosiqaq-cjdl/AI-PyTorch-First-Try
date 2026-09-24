import torch

x = torch.tensor(2.0, requires_grad=True)

y = x **2

print("x:", x)
print("y:", y)

y.backward()

print("x.grad:", x.grad)

x = torch.tensor(3.0, requires_grad = True)

y = 2*x**2 + 5 * x + 1

y.backward()

print("y:", y)
print("gradient:", x.grad)