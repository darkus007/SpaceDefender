"""
Модуль для обработки действий игрока
(перемещение, стрельба, выход из игры).
"""

import pygame
from bullet import Bullet


def events(screen, player, bullets, status):
    """ Обработка действий игрока. """

    for event in pygame.event.get():  # получаем все события

        if event.type == pygame.QUIT:  # выход из игры
            # sys.exit()
            status.in_game = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                player.move_right = True
            if event.key == pygame.K_LEFT:
                player.move_left = True

            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, player)
                bullets.add(new_bullet)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:
                player.move_right = False
            if event.key == pygame.K_LEFT:
                player.move_left = False
