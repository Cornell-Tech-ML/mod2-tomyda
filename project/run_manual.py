"""
Be sure you have minitorch installed in you Virtual Env.
>>> pip install -Ue .
"""

import random

import minitorch
from minitorch import operators

class Network(minitorch.Module):
    def __init__(self):
        super().__init__()
        self.linear = Linear(2, 1)

    def forward(self, x: tuple[float, float]) -> float:
        y = self.linear(x)
        return operators.sigmoid(y[0])


class Linear(minitorch.Module):
    def __init__(self, in_size: int, out_size: int):
        super().__init__()
        random.seed(100)
        self.weights = []
        self.bias = []
        for i in range(in_size):
            weights = []
            for j in range(out_size):
                w = self.add_parameter(f"weight_{i}_{j}", 2 * (random.random() - 0.5))
                weights.append(w)
            self.weights.append(weights)
        for j in range(out_size):
            b = self.add_parameter(f"bias_{j}", 2 * (random.random() - 0.5))
            self.bias.append(b)

    def forward(self, inputs: tuple[float, float]) -> list[float]:
        y = [b.value for b in self.bias]
        for i, x in enumerate(inputs):
            for j in range(len(y)):
                y[j] = y[j] + x * self.weights[i][j].value
        return y


class ManualTrain:
    def __init__(self, hidden_layers: int):
        self.model = Network()

    def run_one(self, x: tuple[float, float]) -> float:
        return self.model.forward((x[0], x[1]))
