"""
Модуль запускает игру "Космический защитник".
"""

from sys import path

path.append(r'SpaceDefender/')

from SpaceDefender.game import Game

if __name__ == "__main__":
    game = Game()
    game.run()
