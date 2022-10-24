"""
Игра "Космический защитник"
Вдохновлена игрой "Space Invaders" 1970 года
"""

import pygame
from pygame.sprite import Group     # контейнер

import control
from bullet import Bullet
from player import Player
from game_logic import *
from text import Text


def run_game():
    pygame.init()
    pygame.display.set_caption("Космический защитник")

    screen_size = 700, 800
    background_color = 0, 0, 0                      # RGB

    screen = pygame.display.set_mode(screen_size)

    player = Player(screen)
    bullets = Group()           # контейнер для пуль
    aliens = Group()            # контейнер для пришельцев
    status = Status(player_lives=3)

    score = Text(screen, "SCORE: ", 0, "left")
    hi_score = Text(screen, "HI SCORE: ", get_hi_score(), "center")
    lives = Text(screen, "LIVES: ", status.player_life, "right")

    Alien.create_aliens_army(screen, aliens)

    while status.in_game:

        control.events(screen, player, bullets, status)

        screen.fill(background_color)

        if len(aliens) == 0:
            new_game(screen, status, player, aliens, bullets, is_win=True)
        else:
            aliens.update()

        bullets.update()
        Bullet.remove_bullets(bullets)
        Bullet.check_collision_and_remove_objects(aliens, bullets, score)

        player.update()
        if player.check_collision(aliens) or Alien.check_end_screen(screen, aliens):
            new_game(screen, status, player, aliens, bullets, is_win=False)
            lives.value = status.player_life

        if score.value > hi_score.value:
            hi_score.value = score.value

        score.update()
        hi_score.update()
        lives.update()

        pygame.display.flip()

    if score.value >= hi_score.value:
        save_hi_score(score.value)


if __name__ == "__main__":
    run_game()
