import random

class BaseCell:
    def __init__(self):
        self.position = (random.randint(0, 49), random.randint(0, 49))
        self.energy = 1.0
        self.alive = True

    def sense(self, environment):
        return {}

    def think(self, environment):
        pass

    def act(self, environment):
        pass

    def move(self, dx, dy, environment):
        new_x = max(0, min(environment.width - 1, self.position[0] + dx))
        new_y = max(0, min(environment.height - 1, self.position[1] + dy))
        self.position = (new_x, new_y)

    def reproduce(self):
        pass
