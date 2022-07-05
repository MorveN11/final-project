##ADDING STATS
import pygame
from pygame.surface import Surface
from epidemic_simulation.utils.constants import WIDTH, HEIGHT, GREY


class StatsGraph:

    def __init__(self, width, heigth, pos_x, pos_y, time):
        self.width = width
        self.heigth = heigth
        self.stats = pygame.Surface(
            (self.width, self.heigth)
        )
        self.pos = (pos_x, pos_y)
        self.T = time

    def configure(self):
        self.stats.fill(GREY)
        self.stats.set_alpha(230)

    def configure_text(self, susceptible, infected, recovered, dead):
        pass

    def update_graph(self):
        pass

    def draw_graph(self):
        pass

    def get_height(self):
        return self.stats.get_height()

    def get_width(self):
        return self.stats.get_width()