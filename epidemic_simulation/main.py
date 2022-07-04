from epidemic_simulation.components.simulation import Simulation

if __name__ == "__main__":
    covid = Simulation()
    covid.n_susceptible = 100
    covid.n_infected = 5
    covid.cycles_to_fate = 200
    covid.mortality_rate = 0.2
    covid.start(randomize=True)
