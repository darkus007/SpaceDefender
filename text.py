"""
Модуль отвечает за вывод информации на экран
(SCORE, HI SCORE, LIVES, LEVEL)
"""

import pygame.font
from pygame import Surface
from typing import Literal


class Text:
    """
    Выводит информацию на экран.

    :param screen: Окно для отрисовки игры (экземпляр класса pygame.Surface).
    :param prefix: Подпись к выводимой информации (например "SCORE:").
    :param value: Выводимая информация.
    :param position_x: Положение на экране по горизонтали, допустимые значения "left", "center", "right".
    :param position_y: Положение на экране по вертикали, допустимые значения "top" (по умолчанию), "center".
    :param font_size: Размер шрифта (по умолчанию 30).
    """

    def __init__(self, screen: Surface, prefix: str, value: int,
                 position_x: Literal["left", "center", "right"],
                 position_y: Literal["top", "center"] = "top",
                 font_size: int = 30):
        self.value = value
        self.position_x = position_x
        self.position_y = position_y
        self.prefix = prefix
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = 139, 195, 74
        self.font = pygame.font.SysFont(None, font_size)
        self.text_to_image()

    def text_to_image(self):
        """ Преобразует текст в графическое изображение. """
        self.text_img = self.font.render(self.prefix + str(self.value), True, self.text_color, (0, 0, 0))
        self.text_rect = self.text_img.get_rect()
        if self.position_x == "left":
            self.text_rect.left = self.screen_rect.left + 40
        if self.position_x == "center":
            self.text_rect.left = self.screen_rect.width / 2 - self.text_rect.width / 2
        if self.position_x == "right":
            self.text_rect.right = self.screen_rect.right - 40
        if self.position_y == "top":
            self.text_rect.top = 8
        elif self.position_y == "center":
            self.text_rect.top = self.screen_rect.height / 2 - self.text_rect.top / 2

    def update(self):
        """ Рисует текст на экране. """
        self.text_to_image()
        self.screen.blit(self.text_img, self.text_rect)
