from epidemic_simulation.components.simulation import Simulation

if __name__ == "__main__":
    simulation = Simulation()
    simulation.n_susceptible = 100
    simulation.n_infected = 5
    simulation.cycles_to_fate = 200
    simulation.mortality_rate = 0.2
    simulation.start(randomize=True)