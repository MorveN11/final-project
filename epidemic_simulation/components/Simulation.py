import sys

import numpy as np
import pygame

from epidemic_simulation.components.Particles import Particles
from epidemic_simulation.utils.constants import WIDTH, HEIGHT, BLUE, GREEN, BACKGROUND, PURPLE, GREY, YELLOW, RED, BLACK


class Simulation:

    def __init__(self, width=WIDTH, height=HEIGHT, susceptible=20, infected=1, t=1000, cycles_to_fate=20, mortality_rate=0.2):
        self.N = None
        self.WIDTH = width
        self.HEIGHT = height

        self.susceptible_container = pygame.sprite.Group()
        self.infected_container = pygame.sprite.Group()
        self.recovered_container = pygame.sprite.Group()
        self.death_container = pygame.sprite.Group()
        self.all_container = pygame.sprite.Group()

        self.n_susceptible = susceptible
        self.n_infected = infected
        self.T = t

        self.cycles_to_fate = cycles_to_fate
        self.mortality_rate = mortality_rate

    # create N particles with the specified color and return a list with the particles.
    def create_particles(self, n, randomize, color):
        list_guy = []
        for i in range(n):
            x = np.random.randint(0, self.WIDTH + 1)
            y = np.random.randint(0, self.HEIGHT + 1)
            vel = np.random.rand(2) * 2 - 1
            guy = Particles(x, y, WIDTH, HEIGHT, color=color, velocity=vel, randomize=randomize)
            list_guy.append(guy)
        return list_guy

    def init_particles(self, susceptible=100, infected=5, randomize=False):
        susceptible_particles = self.create_particles(susceptible, randomize, color=(224, 224, 224))
        infected_particles = self.create_particles(infected, randomize, color=RED)
        self.susceptible_container.add(susceptible_particles)
        self.infected_container.add(infected_particles)
        self.all_container.add(susceptible_particles, infected_particles)


    def init_stats(self):
        pass

    def update(self):
        pass

    def check_collide(self):
        pass

    def setup(self):
        pass

    # generates all the stuff needed to simulate.
    def start(self, susceptible=100, infected=5, randomize=False):
        self.N = self.n_susceptible + self.n_infected
        pygame.init()
        screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])

        self.init_particles(susceptible=susceptible, infected=infected, randomize=randomize)

        ##ADDING STATS
        stats = pygame.Surface(
            (self.WIDTH // 4, self.HEIGHT // 4)
        )

        stats.fill(GREY)
        stats.set_alpha(230)
        stats_pos = (self.WIDTH // 40, self.HEIGHT // 40)

        clock = pygame.time.Clock()
        for i in range(self.T):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.all_container.update()
            screen.fill(BACKGROUND)

            # If susceptible group collide with an infected group. Removes the group.
            ##update stats
            stats_height = stats.get_height()
            stats_width = stats.get_width()
            n_infected_now = len(self.infected_container)
            n_population_now = len(self.all_container)
            n_recovery_now = len(self.recovered_container)

            t = int((i / self.T) * stats_width)
            y_infected = int(stats_height - (n_infected_now / n_population_now) * stats_height)
            y_dead = int(((self.N - n_population_now) / self.N) * stats_height)
            y_recovered = int((n_recovery_now / n_population_now) * stats_height)
            stats_graph = pygame.PixelArray(stats)
            stats_graph[t, y_infected:] = pygame.Color(*RED)
            stats_graph[t, :y_dead] = pygame.Color(*BLACK)
            stats_graph[t, y_dead:y_dead + y_recovered] = pygame.Color(*GREEN)
            # infection
            ## if susceptible group collide with infected group. Removes the group
            collision_group = pygame.sprite.groupcollide(
                self.susceptible_container,
                self.infected_container,
                True,
                False,
            )

            for guy in collision_group:
                new_guy = guy.respawn(RED)
                new_guy.vel *= -1
                new_guy.kill_switch(
                    self.cycles_to_fate,
                    self.mortality_rate
                )
                self.infected_container.add(new_guy)
                self.all_container.add(new_guy)
            # any recoveries?
            recovered = []
            for guy in self.infected_container:
                if guy.is_recovered():
                    new_guy = guy.respawn(GREEN)
                    self.recovered_container.add(new_guy)
                    self.all_container.add(new_guy)
                    recovered.append(guy)
            if len(recovered) > 0:
                self.infected_container.remove(*recovered)
                self.all_container.remove(*recovered)

            del stats_graph
            stats.unlock()
            screen.blit(stats, stats_pos)
            self.all_container.draw(screen)
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()
