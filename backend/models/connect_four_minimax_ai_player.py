# import random
#
#
# class ConnectFourMiniMaxAIPlayer:
#
#     def __init__(self, name, connect_four_game):
#         if name not in [connect_four_game.player_1_name, connect_four_game.player_2_name]:
#             raise ValueError("Can't play in a game that i am not a player")
#         self._name = name
#         self._connect_four_game = connect_four_game
#
#     @property
#     def name(self):
#         return self._name
#
#     def play(self):
#         if self._connect_four_game.current_player == self._name and not self._connect_four_game.is_over:
#             available_moves = self._connect_four_game.available_column_numbers
#             self._connect_four_game.drop_checker_on_column(available_moves[random.randint(0, len(available_moves) - 1)])
#
#     def _minimax(self, depth):
#         available_moves = self._connect_four_game.available_column_numbers
#         board = self._connect_four_game.board(self._name)
#         is_terminal_node = detph == 0 or is_over(board)
#         if depth == 0 or is_terminal_node:
#             if is_terminal_node:
#
