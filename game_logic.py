"""
Модуль отвечает за хранение состояния игры,
содержит игровую логику,
сохраняет и читает рекорды игры.
"""

from pygame import Surface
from pygame.sprite import Group
from os.path import isfile

from aliens import Alien
from player import Player


class Status:
    """ Класс для хранения состояния игры. """

    def __init__(self, player_lives):
        self.in_game = True
        self.game_level = 1
        self.is_alive_player = True
        self.player_life = player_lives


def new_game(screen: Surface, status: Status, player: Player, aliens: Group,
             bullets: Group, is_win: bool) -> None:
    """
    Создает новую игру.

    :param screen: Окно для отрисовки игры (экземпляр класса pygame.Surface).
    :param status: Класс для хранения состояния игры.
    :param player: Игрок.
    :param aliens: Контейнер (pygame.sprite.Group) с пришельцами.
    :param bullets: Контейнер (pygame.sprite.Group) с пулями.
    :param is_win: Игрок победил?
    """
    if is_win:
        status.game_level += 1
    else:
        status.player_life -= 1
        if status.player_life <= 0:
            status.in_game = False
    bullets.empty()
    aliens.empty()
    player.reset()
    Alien.create_aliens_army(screen, aliens)


def get_hi_score() -> int:
    """ Читает рекорд прошлых игр из файла. """
    if isfile('res/hiscore'):
        with open('res/hiscore', 'r') as file:
            hi_score = int(file.read())
        return hi_score
    return 0


def save_hi_score(hi_score: int | str) -> None:
    """ Сохраняет рекорд в файл. """
    with open('res/hiscore', 'w') as file:
        file.write(str(hi_score))
