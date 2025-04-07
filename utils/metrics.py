def compute_fitness(cell):
    return cell.energy if cell.alive else 0

def average_energy(cells):
    energies = [cell.energy for cell in cells if cell.alive]
    return sum(energies) / len(energies) if energies else 0
