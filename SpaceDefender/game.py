"""
Игра "Космический защитник".
Вдохновлена игрой "Space Invaders" 1970 года.

Модуль отвечает за хранение состояния игры,
содержит игровую логику,
сохраняет и читает рекорды игры.
"""

import pygame
from pygame.sprite import Group

import control
from aliens import Alien
from bullet import Bullet
from player import Player
from text import Text
from settings import *
from file import *


class Game:
    """
    Игра "Космический защитник".
    Вдохновлена игрой "Space Invaders" 1970 года.
    Перемещение игрока стрелками "Влево" и "Вправо", "Пробел" - выстрел.
    """

    def __init__(self):
        self.in_game = True
        self.game_level = 0
        self.show_game_level = True
        self.show_game_level_counter = 0
        self.show_game_level_counter_max_value = SHOW_GAME_LEVEL_COUNTER_MAX_VALUE
        self.player_win = True
        self.is_alive_player = True
        self.player_life = PLAYER_LIVES

        pygame.init()
        pygame.display.set_caption("Космический защитник")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        self.player = Player(self.screen)
        self.bullets = Group()  # контейнер для пуль
        self.aliens = Group()  # контейнер для пришельцев

        self.score = Text(self.screen, "SCORE: ", 0, "left")
        self.hi_score = Text(self.screen, "HI SCORE: ", get_hi_score(), "center")
        self.lives = Text(self.screen, "LIVES: ", self.player_life, "right")
        self.level = Text(self.screen, "LEVEL: ", self.game_level, "center", "center", 40)
        self.info = Group(self.score, self.hi_score, self.lives, self.level)

    def new(self):
        """ Создает новую игру. """
        if self.player_win:
            self.game_level += 1
        else:
            self.player_life -= 1
            if self.player_life <= 0:
                self.in_game = False
        self.bullets.empty()
        self.aliens.empty()
        self.player.reset()
        Alien.create_aliens_army(self.screen, self.aliens)

    def draw_game_level_flag_update(self):
        """
        Опускает флаг "Показывать уровень игры" по
        истечению счетчика, заданного SHOW_GAME_LEVEL_COUNTER_MAX_VALUE.
        """
        if self.level.show:
            self.show_game_level_counter += 1
            if self.show_game_level_counter >= SHOW_GAME_LEVEL_COUNTER_MAX_VALUE:
                self.level.show = False
                self.show_game_level_counter = 0

    def run(self):
        """ Запускает игру. """
        while self.in_game:  # основной цикл игры

            self.clock.tick(FPS)

            control.events(self.screen, self.player, self.bullets, self)

            self.screen.fill(BACKGROUND_COLOR)

            self.info.update()
            self.draw_game_level_flag_update()

            if self.score.value > self.hi_score.value:  # динамическое обновление лучшего результата
                self.hi_score.value = self.score.value

            if len(self.aliens) == 0:  # условие победы
                self.new()
                self.level.show = True
                self.level.value = self.game_level
                Alien.speed += ALIEN_SPEED_INCREMENT  # увеличение сложности через ускорение пришельцев
            else:
                self.aliens.update()

            self.bullets.update()
            Bullet.remove_bullets(self.bullets)
            Bullet.check_collision_and_remove_objects(self.aliens, self.bullets, self.score)

            self.player.update()
            if self.player.check_collision(self.aliens) \
                    or Alien.check_end_screen(self.screen, self.aliens):  # условие проигрыша
                self.new()
                self.player_life -= 1
                self.lives.value = self.player_life
                self.level.show = True
                if self.player_life <= 0:
                    self.in_game = False

            pygame.display.flip()

    def __del__(self):
        """ Сохраняет рекорд после завершения игры. """
        check_and_save_hi_score(self.score.value, self.hi_score.value)
        pygame.quit()
