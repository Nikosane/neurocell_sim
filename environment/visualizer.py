import matplotlib.pyplot as plt
import numpy as np

def draw_grid(cells, width, height):
    grid = np.zeros((height, width))
    for cell in cells:
        x, y = cell.position
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = 1

    plt.imshow(grid, cmap='viridis')
    plt.title("Neural Microorganism Simulation")
    plt.pause(0.01)
    plt.clf()
