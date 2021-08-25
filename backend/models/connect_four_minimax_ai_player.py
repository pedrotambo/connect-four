# import random
# import copy
# import itertools
# import math
#
#
# class ConnectFourMiniMaxAIPlayer:
#
#     def __init__(self, name, connect_four_game):
#         if name not in [connect_four_game.player_1_name, connect_four_game.player_2_name]:
#             raise ValueError("Can't play in a game that i am not a player")
#         self._name = name
#         self._connect_four_game = connect_four_game
#         self._board = copy.deepcopy(self._connect_four_game.board(self._name))
#         height = len(self._board)
#         width = len(self._board[0])
#         self._next_free_row = [0 for _ in range(width)]
#         for col in range(width):
#             for row in range(height):
#                 if self._board[row][col] == 0:
#                     self._next_free_row[col] = row
#                     break
#         self._checkers_quantity = sum([1 if self._board[row][col] != 0 else 0 for (row, col) in itertools.product(range(height), range(width))])
#         self._player_number = 1 if connect_four_game.player_1_name == name else 2
#
#     @property
#     def name(self):
#         return self._name
#
#     def play(self):
#         if self._connect_four_game.current_player == self._name and not self._connect_four_game.is_over:
#             available_moves = self._connect_four_game.available_column_numbers(self._name)
#             board = copy.deepcopy(self._connect_four_game.board(self._name))
#             winners = self._board_winners(board)
#             available_column_numbers = self._available_column_numbers(board)
#             self._connect_four_game.drop_checker_on_column(available_moves[random.randint(0, len(available_moves) - 1)])
#
#     def _board_winners(self, board):
#         height = len(board)
#         width = len(board[0])
#         horizontal_winners = self._board_winners_width_direction(board, range(height), range(width - 3), 0, 1)
#         vertical_winners = self._board_winners_width_direction(board, range(height - 3), range(width), 1, 0)
#         main_diagonal_winners = self._board_winners_width_direction(board, range(3, height), range(width - 3), -1, 1)
#         anti_main_diagonal_winners = self._board_winners_width_direction(board, range(3, height), range(3, width), -1,
#                                                                          -1)
#         return horizontal_winners | vertical_winners | main_diagonal_winners | anti_main_diagonal_winners
#
#     def _board_winners_width_direction(self, board, row_range, col_range, row_increment, col_increment):
#         winners = []
#         for (row, col) in itertools.product(row_range, col_range):
#             line = [board[row + i * row_increment][col + i * col_increment] for i in range(4)]
#             all_elements_in_line_are_equal = len(set(line)) == 1
#             if line[0] != 0 and all_elements_in_line_are_equal:
#                 winners.append(board[row][col])
#         return set(winners)
#
#     def _available_column_numbers(self, board):
#         height = len(board)
#         width = len(board[0])
#         available_columns_numbers = set()
#         for (row, col) in itertools.product(range(height), range(width)):
#             if board[row][col] == 0:
#                 available_columns_numbers.add(col)
#         return available_columns_numbers
#
#
#     def _minimax(self, depth, board, ):
#
#     # def _minimax(self, depth, board, isMaximizingPlayer):
#     #     height = len(board)
#     #     width = len(board[0])
#     #     available_moves = self._available_column_numbers(board)
#     #     winners = self._board_winners(board)
#     #     if len(winners) > 1:
#     #         raise ValueError("ERROR! THIS SHOULDN'T HAPPEN")
#     #     else:
#     #         winner = [w for w in winners][0] if winners else None
#     #     is_terminal_node = winners or not available_moves
#     #     if depth == 0 or is_terminal_node:
#     #         if is_terminal_node:
#     #             if winner == self._player_number:
#     #                 return (None, 100000000000000)
#     #             elif winner:
#     #                 return (None, -10000000000000)
#     #             else:
#     #                 # game is tied
#     #                 return (None, 0)
#     #     if isMaximizingPlayer:
#     #         value = -math.inf
#     #         column = random.choice(available_moves)
#     #         for col in available_moves:
#     #             row = -1
#     #             for r in range(height):
#     #                 if board[r][col] == 0:
#     #                     row = r
#     #             if row == -1: raise ValueError("THIS SHOULDN'T HAPPEN")
#     #             board[row][col] = self._player_number
#     #             new_score = self._minimax(depth-1, board, False)
#     #             board[row][col] = 0
#     #             if new_score < value:
#     #                 value = new_score
#     #                 column = col
