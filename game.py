"""
Игра "Космический защитник"
Вдохновлена игрой "Space Invaders" 1970 года

Модуль отвечает за хранение состояния игры,
содержит игровую логику,
сохраняет и читает рекорды игры.
"""

import pygame
from pygame import Surface
from pygame.sprite import Group
from os.path import isfile

import control
from aliens import Alien
from bullet import Bullet
from player import Player
from text import Text

FPS = 60


class Status:
    """ Класс для хранения состояния игры. """

    def __init__(self, player_lives):
        self.in_game = True
        self.game_level = 0
        self.show_game_level = True
        self.show_game_level_counter = 0
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


def show_game_level(status: Status, level: Text, show_time: int) -> None:
    """
    Показывает текущий уровень игры.

    :param status: Класс для хранения состояния игры.
    :param level: Экземпляр класса Text, для отображения уровня игры.
    :param show_time: Задержка отображения текущего уровня.
    """
    if status.show_game_level:
        level.update()
        status.show_game_level_counter += 1
        if status.show_game_level_counter >= show_time:
            status.show_game_level = False
            status.show_game_level_counter = 0


def get_hi_score() -> int:
    """ Читает рекорд прошлых игр из файла 'res/hiscore'. """
    if isfile('res/hiscore'):
        with open('res/hiscore', 'r') as file:
            hi_score = int(file.read())
        return hi_score
    return 0


def check_and_save_hi_score(current_score: int, hi_score: int) -> None:
    """ Если установлен новый рекорд, то сохраняет его в файл. """
    if current_score >= hi_score:
        with open('res/hiscore', 'w') as file:
            file.write(str(current_score))


def run_game():
    """ Запускает игру. """

    pygame.init()
    pygame.display.set_caption("Космический защитник")

    screen_size = 700, 800
    background_color = 0, 0, 0                      # RGB

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(screen_size)

    player = Player(screen)
    bullets = Group()           # контейнер для пуль
    aliens = Group()            # контейнер для пришельцев
    status = Status(player_lives=3)

    score = Text(screen, "SCORE: ", 0, "left")
    hi_score = Text(screen, "HI SCORE: ", get_hi_score(), "center")
    lives = Text(screen, "LIVES: ", status.player_life, "right")
    level = Text(screen, "LEVEL: ", status.game_level, "center", "center", 40)

    while status.in_game:       # основной цикл игры

        clock.tick(FPS)

        control.events(screen, player, bullets, status)

        screen.fill(background_color)

        score.update()
        hi_score.update()
        lives.update()
        show_game_level(status, level, show_time=FPS)

        if score.value > hi_score.value:    # динамическое обновление лучшего результата
            hi_score.value = score.value

        if len(aliens) == 0:
            new_game(screen, status, player, aliens, bullets, is_win=True)
            status.show_game_level = True
            level.value = status.game_level
        else:
            aliens.update()

        bullets.update()
        Bullet.remove_bullets(bullets)
        Bullet.check_collision_and_remove_objects(aliens, bullets, score)

        player.update()
        if player.check_collision(aliens) or Alien.check_end_screen(screen, aliens):
            new_game(screen, status, player, aliens, bullets, is_win=False)
            lives.value = status.player_life
            status.show_game_level = True

        pygame.display.flip()

    check_and_save_hi_score(score.value, hi_score.value)
    pygame.quit()
