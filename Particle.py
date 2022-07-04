import numpy as np
import pygame, sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = WHITE
BLUE = (0, 100, 255)


class Particle(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color=BLACK, radius=5, velocity=[0, 0]):
        super().__init__()
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


WIDTH = 600
HEIGHT = 400
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
container = pygame.sprite.Group()

for i in range(100):
    x = np.random.randint(0, WIDTH + 1)
    y = np.random.randint(0, HEIGHT + 1)
    vel = np.random.rand(2) * 2 - 1
    guy = Particle(x, y, WIDTH, HEIGHT, color=BLUE, velocity=vel)
    container.add(guy)

T = 1000

clock = pygame.time.Clock()

for i in range(T):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    container.update()
    screen.fill(BACKGROUND)
    container.draw(screen)
    pygame.display.flip()
    clock.tick(30)
