##ADDING STATS
from pygame.surface import Surface
from epidemic_simulation.utils.constants import  WIDTH, HEIGHT

class Graphstats(Surface):

    def __init__(self):

        super((WIDTH // 4, HEIGHT // 4))

        stats.fill(GREY)
        stats.set_alpha(230)
        stats_pos = (self.WIDTH // 40, self.HEIGHT // 40)