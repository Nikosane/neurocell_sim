import numpy as np

class SimpleNeuralNet:
    def __init__(self, input_size, hidden_size, output_size):
        self.w1 = np.random.randn(hidden_size, input_size)
        self.b1 = np.zeros(hidden_size)
        self.w2 = np.random.randn(output_size, hidden_size)
        self.b2 = np.zeros(output_size)

    def forward(self, x):
        h = np.tanh(np.dot(self.w1, x) + self.b1)
        output = np.tanh(np.dot(self.w2, h) + self.b2)
        return output

    def parameters(self):
        return [self.w1, self.b1, self.w2, self.b2]
