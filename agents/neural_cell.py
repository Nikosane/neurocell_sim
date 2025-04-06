from agents.base_cell import BaseCell
from models.network import SimpleNeuralNet
import numpy as np
import random

class NeuralCell(BaseCell):
    def __init__(self):
        super().__init__()
        self.brain = SimpleNeuralNet(input_size=4, hidden_size=6, output_size=2)

    def sense(self, environment):
        x, y = self.position
        nutrient = environment.nutrient_map[y][x] if environment.nutrient_map else 0
        return np.array([nutrient, self.energy, x / environment.width, y / environment.height])

    def think(self, environment):
        inputs = self.sense(environment)
        self.output = self.brain.forward(inputs)

    def act(self, environment):
        dx = int(np.clip(self.output[0], -1, 1))
        dy = int(np.clip(self.output[1], -1, 1))
        self.move(dx, dy, environment)
        self.energy -= 0.01

