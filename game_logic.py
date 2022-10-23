from aliens import Alien

class Status:
    def __init__(self, player_life):
        self.in_game = True
        self.game_level = 1
        self.is_alive_player = True
        self.player_life = player_life


def init_game():
    pass


def new_game(screen, status, player, aliens, bullets, is_win):
    if is_win:
        status.game_level += 1
        print(status.game_level)
    else:
        status.player_life -= 1
        print(status.player_life)
        if status.player_life <= 0:
            status.in_game = False
    bullets.empty()
    aliens.empty()
    player.reset()
    Alien.create_aliens_army(screen, aliens)


def new_level():
    pass
