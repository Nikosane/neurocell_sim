import random

class PetriDish:
    def __init__(self, width, height, nutrient_map=True):
        self.width = width
        self.height = height
        self.grid = [[[] for _ in range(width)] for _ in range(height)]
        self.cells = []
        self.nutrient_map = self._generate_nutrients() if nutrient_map else None

    def _generate_nutrients(self):
        return [[random.uniform(0, 1) for _ in range(self.width)] for _ in range(self.height)]

    def add_cell(self, cell):
        self.cells.append(cell)
        x, y = cell.position
        self.grid[y][x].append(cell)

    def update(self):
        for cell in self.cells:
            cell.think(self)
            cell.act(self)

    def save_state(self):
        pass  # Will implement save functionality

    def visualize(self):
        pass  # Hook for visualization
