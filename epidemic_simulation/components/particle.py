import numpy as np
import pygame

from epidemic_simulation.utils.constants import BACKGROUND, BLACK


class Particle(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color=BLACK, radius=5, velocity=None, randomize=False):
        super().__init__()
        self.mortality_rate = None
        self.cycles_to_fate = None
        if velocity is None:
            velocity = [0, 0]
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(BACKGROUND)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.pos = np.array([x, y])
        self.pos = self.pos.astype(np.float64)
        self.vel = np.asarray(velocity)
        self.vel = self.vel.astype(np.float64)

        self.WIDTH = width
        self.HEIGHT = height

        self.killSwitch_on = False
        self.recovered = False

        self.randomize = randomize

    def update(self):
        self.pos += self.vel
        x, y = self.pos
        if x < 0:
            self.pos[0] = self.WIDTH
            x = self.WIDTH
        if x > self.WIDTH:
            self.pos[0] = 0
            x = 0
        if y < 0:
            self.pos[1] = self.HEIGHT
            y = self.HEIGHT
        if y > self.HEIGHT:
            self.pos[1] = 0
            x = 0

        self.rect.x = x
        self.rect.y = y

        vel_norm = np.linalg.norm(self.vel)
        if vel_norm > 3:
            self.vel /= vel_norm

        if self.randomize:
            # self.vel += np.random.rand(2) * 2 -1
            self.vel = self.vel

        if self.killSwitch_on:
            self.cycles_to_fate -= 1
            if self.cycles_to_fate <= 0:
                self.killSwitch_on = False
                some_number = np.random.rand()
                if self.mortality_rate > some_number:
                    self.kill()
                else:
                    self.recovered = True

    # return a new particle with the same attributes but with different color.
    def respawn(self, color):
        return Particle(
            self.rect.x,
            self.rect.y,
            self.WIDTH,
            self.HEIGHT,
            color=color,
            velocity=self.vel
        )

    #
    def killSwitch(self, cycles_to_fate=20, mortality_rate=0.2):
        self.killSwitch_on = True
        self.cycles_to_fate = cycles_to_fate
        self.mortality_rate = mortality_rate

    # getter of recovered attribute
    def is_recovered(self):
        return self.recovered
