import pygame

from epidemic_simulation.utils.constants import *
from epidemic_simulation.components.partcles import Particles
from epidemic_simulation.utils import text_utils


class Simulation:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Particles()
        self.playing = False
        self.running = True
        self.game_speed = 20
        self.points = 0

    def run(self):
        self.points = 0
        self.game_speed = 20
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                quit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True
        self.screen.fill(WHITE)
        self.draw_inputs()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                # verificado
                self.run()

    def draw_inputs(self):
        txt, txt_rect = text_utils.get_centered_message("Inputs")
        self.screen.blit(txt, txt_rect)
