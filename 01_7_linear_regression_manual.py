import torch

x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([3.0, 5.0, 7.0])

w = torch.tensor(0.0, requires_grad = True)
b = torch.tensor(0.0, requires_grad = True)

learning_rate = 0.01

for epoch in range(100):
    y_pred = w * x + b

    loss = ((y_pred - y) ** 2).mean()

    loss.backward()

    with torch.no_grad():
        w -= learning_rate*w.grad
        b -= learning_rate*b.grad

    w.grad.zero_()
    b.grad.zero_()

    if epoch % 10 == 0:
        print(
            f"Epoch {epoch}: "
            f"loss={loss.item():.4f}, "
            f"w={w.item():.4f}, "
            f"b={b.item():.4f}"
        )