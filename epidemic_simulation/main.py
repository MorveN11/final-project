from epidemic_simulation.components.simulation import Simulation

if __name__ == "__main__":
    covid = Simulation()
    covid.n_susceptible = 80
    covid.cycles_to_fate = 200
    covid.start(randomize=True)
