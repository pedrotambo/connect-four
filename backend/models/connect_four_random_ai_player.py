import random


class ConnectFourRandomAIPlayer:

    def __init__(self, name, connect_four_game):
        if name not in [connect_four_game.player_1_name, connect_four_game.player_2_name]:
            raise ValueError("Can't play in a game that it's not a player")
        self._name = name
        self._connect_four_game = connect_four_game

    @property
    def name(self):
        return self._name

    def play(self):
        if self._connect_four_game.current_player == self._name:
            available_moves = self._connect_four_game.available_column_numbers()
            self._connect_four_game.drop_checker_on_column(available_moves[random.randint(0, len(available_moves))])
