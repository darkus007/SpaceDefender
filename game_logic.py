from aliens import Alien
from os.path import isfile


class Status:
    def __init__(self, player_lives):
        self.in_game = True
        self.game_level = 1
        self.is_alive_player = True
        self.player_life = player_lives


def new_game(screen, status, player, aliens, bullets, is_win):
    """
    Создает новую игру
    :param screen: Экземпляр класса pygame.Surface.
    :param status:
    :param player:
    :param aliens:
    :param bullets:
    :param is_win:
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
    """ Читает рекорд прошлых игр из файла """
    if isfile('res/hiscore'):
        with open('res/hiscore', 'r') as file:
            hi_score = int(file.read())
        return hi_score
    return 0


def save_hi_score(hi_score: int | str) -> None:
    """ Сохраняет рекорд в файл """
    with open('res/hiscore', 'w') as file:
        file.write(str(hi_score))
