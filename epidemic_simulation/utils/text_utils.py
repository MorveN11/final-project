import pygame

from epidemic_simulation.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = "freesansbold.ttf"
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)


def get_score_element(points, dark):
    font = pygame.font.Font(FONT_STYLE, 22)
    if not dark:
        text = font.render("Points: " + str(points), True, BLACK_COLOR)
    else:
        text = font.render("Points: " + str(points), True, WHITE_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return text, text_rect


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2, size=30):
    font = pygame.font.Font(FONT_STYLE, size)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
