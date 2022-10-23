import pygame
from pygame.sprite import Group

# наследуем от класса Sprite - предназначен для отображения анимированных объектов
from score import Score


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, player):
        super(Bullet, self).__init__()
        self.screen = screen
        self.is_alive = True

        # создаем пулю
        self.rect = pygame.Rect(0, 0, 2, 12)  # размер
        self.color = 139, 195, 74  # цвет
        self.speed = 3

        # начальное положение пули от положения игрока
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top

    def _move(self):
        """ Перемещает пулю """
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.is_alive = False

    # переопределение метода из класса Sprite для отрисовки пуль
    def update(self):
        """ Рисует пулю и проверяет коллизию с пришельцами """
        self._move()
        pygame.draw.rect(self.screen, self.color, self.rect)

    @staticmethod
    def remove_bullets(bullets: Group) -> None:
        """ Удаляет пули, которые вышли за пределы экрана """
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

    @staticmethod
    def check_collision_and_remove_objects(aliens: Group, bullets: Group, score: Score) -> None:
        """ Проверяет коллизию между пулями и пришельцами, при ее наличии удаляет пулю и пришельца """
        # создает словарь Dict[bullets: aliens]; ключи True, True - означают удалять и пулю и пришельца
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        score.value += len(collisions.values())  # увеличивает счет на количество пораженных пришельцев


