import random
import itertools
import copy


class ConnectFourSimplisticAIPlayer:

    def __init__(self, name, connect_four_game):
        if name not in [connect_four_game.player_1_name, connect_four_game.player_2_name]:
            raise ValueError("Can't play in a game that i am not a player")
        self._name = name
        self._connect_four_game = connect_four_game
        self._board = copy.deepcopy(self._connect_four_game.board(self._name))
        self._height = len(self._board)
        self._width = len(self._board[0])
        self._player_number = 1 if connect_four_game.player_1_name == name else 2

    @property
    def name(self):
        return self._name

    def play(self):
        if not self._connect_four_game.current_player == self._name or self._connect_four_game.is_over:
            raise ValueError("Can't play when it's not my turn or game is over.")
        available_moves = self._connect_four_game.available_column_numbers(self._name)
        board = self._connect_four_game.board(self._name)
        winner_moves = list(filter(lambda move: move in available_moves, self.winner_moves(board)))
        three_liner_moves = list(filter(lambda move: move in available_moves, self.three_liner_moves(board)))
        if winner_moves:
            self._connect_four_game.drop_checker_on_column(random.choice(winner_moves))
        elif three_liner_moves:
            self._connect_four_game.drop_checker_on_column(random.choice(three_liner_moves))
        else:
            self._connect_four_game.drop_checker_on_column(random.choice(available_moves))

    def _available_column_numbers(self, board):
        height = len(board)
        width = len(board[0])
        available_columns_numbers = set()
        for (row, col) in itertools.product(range(height), range(width)):
            if self._board[row][col] == 0:
                available_columns_numbers.add(col)
        return available_columns_numbers

    def winner_moves(self, board):
        width = len(board[0])
        height = len(board)
        h_move = self._directed_winner_move(board, range(height), range(width - 3), 0, 1)
        v_move = self._directed_winner_move(board, range(height - 3), range(width), 1, 0)
        md_move = self._directed_winner_move(board, range(3, height), range(width - 3), -1, 1)
        ad_move = self._directed_winner_move(board, range(3, height), range(3, width), -1, -1)
        return list(filter(lambda move: move is not None, [h_move, v_move, md_move, ad_move]))

    def _directed_winner_move(self, board, row_range, col_range, row_increment, col_increment):
        for (row, col) in itertools.product(row_range, col_range):
            if board[row][col] == self._player_number:
                two_next_checkers = [board[row + i * row_increment][col + i * col_increment] for i in range(1, 3)]
                all_own_checkers = all([True if elem == self._player_number else False for elem in two_next_checkers])
                next_row = row + 3 * row_increment
                next_col = col + 3 * col_increment
                if all_own_checkers and board[next_row][next_col] == 0 and self._below_is_not_empty(board, next_row,
                                                                                                    next_col):
                    return next_col
            elif board[row][col] == 0:
                three_next_checkers = [board[row + i * row_increment][col + i * col_increment] for i in range(1, 4)]
                all_own_checkers = all([True if elem == self._player_number else False for elem in three_next_checkers])
                if all_own_checkers and self._below_is_not_empty(board, row, col):
                    return col
        return None

    def three_liner_moves(self, board):
        width = len(board[0])
        height = len(board)
        h_move = self._directed_three_liner_move(board, range(height), range(width - 3), 0, 1)
        v_move = self._directed_three_liner_move(board, range(height - 3), range(width), 1, 0)
        md_move = self._directed_three_liner_move(board, range(3, height), range(width - 3), -1, 1)
        ad_move = self._directed_three_liner_move(board, range(3, height), range(3, width), -1, -1)
        return list(filter(lambda move: move is not None, [h_move, v_move, md_move, ad_move]))

    def _directed_three_liner_move(self, board, row_range, col_range, row_increment, col_increment):
        for (row, col) in itertools.product(row_range, col_range):
            if board[row][col] == self._player_number:
                next_own_checker = True if board[row + row_increment][col + col_increment] == self._player_number else False
                next_two_checkers_after = [board[row + i * row_increment][col + i * col_increment] for i in range(2, 4)]
                empty_next_two_checkers_after = all(
                    [True if elem == 0 else False for elem in next_two_checkers_after]
                )
                potential_col = col + 2 * col_increment
                if next_own_checker and empty_next_two_checkers_after and self._below_is_not_empty(board, row, potential_col):
                    return col + 2 * col_increment
            elif board[row][col] == 0:
                if board[row][col + 1 * col_increment] == self._player_number:
                    two_next_checkers = [board[row + i * row_increment][col + i * col_increment] for i in range(1, 3)]
                    own_two_next_checkers = all(
                        [True if elem == self._player_number else False for elem in two_next_checkers])
                    four_checker_is_empty = board[row + 3 * row_increment][col + 3 * col_increment] == 0
                    if own_two_next_checkers and four_checker_is_empty and self._below_is_not_empty(board, row, col):
                        return col
                else:
                    next_two_checkers_after_next = [board[row + i * row_increment][col + i * col_increment] for i in range(2, 4)]
                    own_next_two_checkers_after_next = all(
                        [True if elem == self._player_number else False for elem in next_two_checkers_after_next])
                    if own_next_two_checkers_after_next and self._below_is_not_empty(board, row + 1 * row_increment, col + 1 * col_increment):
                        return col + 1 * col_increment
        return None

    def _below_is_not_empty(self, board, row, col):
        return True if row == 5 else board[row + 1][col] != 0

    def _is_valid_move(self, board, row, col):
        width = len(board[0])
        height = len(board)
        return 0 <= row < height and 0 <= col < width and True if row == 0 else board[row - 1][col] != 0


