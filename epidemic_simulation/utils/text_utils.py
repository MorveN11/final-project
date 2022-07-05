import pygame

from epidemic_simulation.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = pygame.font.get_default_font()
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)


def get_element(points, type_of_group, pos_x, pos_y):
    font = pygame.font.Font(FONT_STYLE, 16)
    text = font.render("Total " + type_of_group + ": " + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (pos_x, pos_y)
    return text, text_rect


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2, size=30):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
