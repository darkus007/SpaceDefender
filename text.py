import pygame.font
from pygame import Surface
from typing import Literal


class Text:
    """
    Выводит информацию на экран.

    :param screen: Экземпляр класса pygame.Surface.
    :param prefix: Подпись к выводимой информации (например "SCORE:").
    :param value: Выводимая информация.
    :param position: Положение на экране, допустимые значения "left", "center", "right".
    """
    def __init__(self, screen: Surface, prefix: str, value: int, position: Literal["left", "center", "right"]):
        self.value = value
        self.position = position
        self.prefix = prefix
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = 139, 195, 74
        self.font = pygame.font.SysFont(None, 36)
        self.text_to_image()

    def text_to_image(self):
        """ Преобразует текст в графическое изображение """
        self.text_img = self.font.render(self.prefix + str(self.value), True, self.text_color, (0, 0, 0))
        self.text_rect = self.text_img.get_rect()
        if self.position == "left":
            self.text_rect.left = self.screen_rect.left + 40
        if self.position == "center":
            self.text_rect.left = self.screen_rect.width / 2 - self.text_rect.width / 2
            pass
        if self.position == "right":
            self.text_rect.right = self.screen_rect.right - 40
        self.screen_rect.top = 10

    def update(self):
        """ Рисует текст на экране """
        self.text_to_image()
        self.screen.blit(self.text_img, self.text_rect)
