"""
Модуль отвечает за создание и отображение пришельцев.
"""

from pygame import Surface, image
from pygame.sprite import Group, Sprite


class Alien(Sprite):
    """
    Создает пришельца.

    Наследуется от класса pygame.sprite.Sprite, что позволяет добавлять его
    в класс - контейнер pygame.sprite.Group.
    Класс Group имеет метод update(), который вызывает аналогичный метод
    update() для каждого члена класса.

    :param screen: Окно для отрисовки игры (экземпляр класса pygame.Surface).
    """

    speed = 0.4

    def __init__(self, screen: Surface):
        super(Alien, self).__init__()
        self.screen = screen
        self.image = image.load('res/alien.png')
        self.rect = self.image.get_rect()  # все объекты в виде прямоугольников
        self.alien_width = self.rect.width
        self.alien_height = self.rect.height
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def _move_alien(self):
        """ Перемещает пришельца. """
        self.y += self.speed
        self.rect.y = self.y

    def update(self):
        """ Рисует пришельца. """
        self._move_alien()
        self.screen.blit(self.image, self.rect)

    @staticmethod
    def create_aliens_army(screen: Surface, aliens_container: Group) -> None:
        """ Создает армию пришельцев. """
        space_between_aliens_x = 4  # px
        space_between_aliens_y = 20  # px
        rows_aliens = 4  # штук

        alien_width = Alien(screen).alien_width
        number_aliens_on_x = int((screen.get_rect().width - 2 * alien_width) / alien_width)
        gap_x = int((screen.get_rect().width - (alien_width + space_between_aliens_x) * number_aliens_on_x) / 2)

        for alien_row in range(rows_aliens):
            for alien_number in range(number_aliens_on_x):
                alien = Alien(screen)
                alien.rect.x = gap_x + (alien.alien_width + space_between_aliens_x) * alien_number
                alien.rect.y = alien.alien_height + (alien.alien_height + space_between_aliens_y) * alien_row
                alien.y = alien.rect.y
                aliens_container.add(alien)

    @staticmethod
    def check_end_screen(screen: Surface, aliens_container: Group) -> bool:
        """ Проверяет дошли ли пришельцы до конца экрана. """
        screen_bottom = screen.get_rect().bottom
        for alien in aliens_container:
            if alien.rect.bottom >= screen_bottom:
                return True
        return False
