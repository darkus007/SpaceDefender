import pygame.font


class Score:
    def __init__(self, screen, prefix: str, value: int):
        self.value = value
        self.prefix = prefix
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = 139, 195, 74
        self.font = pygame.font.SysFont(None, 36)
        self.text_to_image()

    def text_to_image(self):
        """ Преобразует текст в графическое изображение """
        self.score_img = self.font.render(self.prefix + str(self.value), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = self.screen_rect.left + 10
        self.screen_rect.top = 5

    def update(self):
        """ Рисует текст на экране """
        self.text_to_image()
        self.screen.blit(self.score_img, self.score_rect)
