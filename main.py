"""
Игра "Космический охотник"
Вдохновлена игрой "Space Invaders" 1970 года
"""

import pygame
from pygame.sprite import Group     # контейнер

import control
from bullet import Bullet
from player import Player
from game_logic import *
from score import Score


def run_game():
    pygame.init()
    pygame.display.set_caption("Космический охотник")

    screen_size = 700, 800
    background_color = 0, 0, 0                      # RGB

    screen = pygame.display.set_mode(screen_size)

    player = Player(screen)
    bullets = Group()           # контейнер для пуль
    aliens = Group()            # контейнер для пришельцев
    status = Status(player_life=3)
    score = Score(screen, "SCORE: ", 0)

    Alien.create_aliens_army(screen, aliens)

    while status.in_game:

        control.events(screen, player, bullets)

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

        score.update()

        pygame.display.flip()


if __name__ == "__main__":
    run_game()
