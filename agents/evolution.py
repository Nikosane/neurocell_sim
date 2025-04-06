import copy
import random
import numpy as np

def mutate(brain, mutation_rate=0.1):
    for param in brain.parameters():
        noise = np.random.randn(*param.shape) * mutation_rate
        param += noise
    return brain

def crossover(parent1, parent2):
    child = copy.deepcopy(parent1)
    for i, param in enumerate(child.parameters()):
        mask = np.random.rand(*param.shape) > 0.5
        param[mask] = parent2.parameters()[i][mask]
    return child
