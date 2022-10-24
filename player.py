"""
Модуль отвечает за создание и отображение игрока.
"""

import pygame
from pygame.sprite import Group, Sprite
from pygame import Surface


class Player(Sprite):
    """
    Создает игрока.

    :param screen: Окно для отрисовки игры (экземпляр класса pygame.Surface).
    """

    speed = 2

    def __init__(self, screen: Surface):
        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('res/player.png')
        self.rect = self.image.get_rect()  # все объекты в виде прямоугольников
        self.screen_rect = screen.get_rect()
        self.reset()
        self.move_right = False
        self.move_left = False

    def _move(self):
        """ Перемещает игрока. """
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= self.speed

    def reset(self):
        """ Сбрасывает позицию игрока в начальную. """
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self):
        """ Рисует игрока """
        self._move()
        self.screen.blit(self.image, self.rect)

    def check_collision(self, aliens: Group) -> bool:
        """ Проверяет коллизию между игроком и пришельцами. """
        if pygame.sprite.spritecollideany(self, aliens):
            return True
        return False
