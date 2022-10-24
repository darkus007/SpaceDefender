"""
Модуль отвечает за создание и отображение пуль.
Проверяет коллизию между пулями и пришельцами, при ее наличии удаляет пулю и пришельца.
"""

import pygame
from pygame import Surface
from pygame.sprite import Group, Sprite

from text import Text
from player import Player


class Bullet(Sprite):
    """
    Создает пулю.

    Наследуется от класса pygame.sprite.Sprite, что позволяет добавлять его
    в класс - контейнер pygame.sprite.Group.
    Класс Group имеет метод update(), который вызывает аналогичный метод
    update() для каждого члена класса.

    :param screen: Окно для отрисовки игры (экземпляр класса pygame.Surface).
    :param player: Игрок, используется для вычисления начальной позиции пули.
    """

    def __init__(self, screen: Surface, player: Player):
        super(Bullet, self).__init__()
        self.screen = screen
        self.is_alive = True

        # создаем пулю
        self.rect = pygame.Rect(0, 0, 2, 12)  # размер
        # self.color = 139, 195, 74  # цвет
        self.color = 255, 0, 0  # цвет
        self.speed = 3

        # начальное положение пули от положения игрока
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

    def _move(self):
        """ Перемещает пулю """
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.is_alive = False

    # переопределение метода класса Sprite для отрисовки пуль
    def update(self):
        """ Рисует пулю """
        self._move()
        pygame.draw.rect(self.screen, self.color, self.rect)

    @staticmethod
    def remove_bullets(bullets: Group) -> None:
        """ Удаляет пули, которые вышли за пределы экрана """
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

    @staticmethod
    def check_collision_and_remove_objects(aliens: Group, bullets: Group, score: Text) -> None:
        """ Проверяет коллизию между пулями и пришельцами, при ее наличии удаляет пулю и пришельца """
        # создает словарь Dict[bullets: aliens]; ключи True, True - означают удалять и пулю и пришельца
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        score.value += len(collisions.values())  # увеличивает счет на количество пораженных пришельцев
