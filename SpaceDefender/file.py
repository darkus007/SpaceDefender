"""
Модуль содержит функции для чтения
и сохранения рекордов игр.
"""

from os.path import isfile, dirname


def get_hi_score() -> int:
    """ Читает рекорд прошлых игр из файла 'res/hiscore'. """
    if isfile('res/hiscore'):
        with open(f'{dirname(__file__)}/res/hiscore', 'r') as file:
            hi_score = int(file.read())
        return hi_score
    return 0


def check_and_save_hi_score(current_score: int, hi_score: int) -> None:
    """ Если установлен новый рекорд, то сохраняет его в файл. """
    if current_score >= hi_score:
        with open(f'{dirname(__file__)}/res/hiscore', 'w') as file:
            file.write(str(current_score))
