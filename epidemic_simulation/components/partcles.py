from epidemic_simulation.utils import text_utils


class Particles:
    def __init__(self):
        pass

    @staticmethod
    def draw(screen):
        txt, txt_rect = text_utils.get_centered_message("Particles")
        screen.blit(txt, txt_rect)

    def update(self, user_input):
        pass
