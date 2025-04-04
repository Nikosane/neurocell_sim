from config import GRID_SIZE, NUM_CELLS, MAX_STEPS, SAVE_INTERVAL
from environment.petri_dish import PetriDish
from agents.neural_cell import NeuralCell

def run_simulation():
    dish = PetriDish(width=GRID_SIZE[0], height=GRID_SIZE[1])

    # Initialize the cells
    for _ in range(NUM_CELLS):
        cell = NeuralCell()
        dish.add_cell(cell)

    # Run the simulation
    for step in range(MAX_STEPS):
        dish.update()

        if step % SAVE_INTERVAL == 0:
            dish.save_state()

        dish.visualize()

if __name__ == "__main__":
    run_simulation()
