# 🧠 Neural Microorganism Simulator

A biologically-inspired simulation where **neural network-controlled microorganisms** evolve, cooperate, fight, and mutate inside a virtual petri dish. This project explores **emergent behavior**, **neural adaptation**, and **survival-driven intelligence** — all running on a local machine.

---

## 🚀 Features

- 🧬 **Neural Network Agents**: Each cell uses a tiny brain to make survival decisions.
- 🌱 **Evolving Ecosystem**: Mutation, crossover, and selective pressure create new strategies over generations.
- ⚔️ **Behavior Diversity**: Cells can eat, flee, reproduce, attack, or signal others.
- 🌡️ **Dynamic Environment**: Nutrients, heat, and hazards change the survival landscape.
- 📊 **Real-time Visualization**: See the petri dish evolve with interactive plots or grid visualizations.

---

## ⚙️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/Nikosane/neurocell_sim.git
cd neurocell_sim
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Simulation

```bash
python main.py
```

Optional flags (coming soon):
- `--headless` to disable visualization
- `--load-last` to resume from the last saved generation

---

## 🧪 Customization

Edit `config.py` to change:
- Cell population
- Grid size
- Mutation rates
- Sensory input ranges
- Neural architecture

---

## 🌍 Simulation Logic

Each tick, every cell:
- **Senses** its local environment (food, neighbors, hazards)
- **Thinks** using a neural network
- **Acts** (move, divide, attack, signal, mutate)

Evolution occurs over generations via:
- Fitness evaluation
- Selection of top performers
- Crossover and mutation

---

## 📈 Future Ideas

- Genetic memory and learned behaviors
- Bioluminescence and cell-to-cell signaling
- Emergent social colonies and swarm dynamics
- Visual neural debugging dashboard

---

## 🤖 Inspiration

This project is inspired by:
- Conway’s Game of Life
- Cellular automata
- Evolutionary neural networks
- Real-world microbiology simulations

---

## 🧑‍💻 Author

Developed by [Nikosane]  
Feel free to fork, modify, and evolve it your way.
