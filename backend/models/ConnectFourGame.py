import itertools


class ConnectFourGame:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._board = [[0 for _ in range(height)] for _ in range(width)]
        self._next_free_row_number_by_column = dict.fromkeys(range(width), 0)
        self._current_player = 1
        self._is_over = False
        self._was_won = False
        self._winner = None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def current_player(self):
        return self._current_player

    @property
    def was_won(self):
        return self._was_won

    @property
    def winner(self):
        return self._winner if self.is_over else None

    @property
    def was_tied(self):
        return not self.was_won and self._board_is_full()

    @property
    def is_over(self):
        return self.was_won or self.was_tied

    def drop_checker_on_column(self, column_number):
        self._validate_move(column_number)
        self._update_game(column_number)

    def _validate_move(self, column_number):
        if not 0 <= column_number < self._width:
            raise ConnectFourException("Can't play on column bigger or equal than the width, or less than 0.")

        if self._next_free_row_number_by_column[column_number] >= self.height:
            raise ConnectFourException(f'Column {column_number} is full.')

        if self.is_over:
            raise ConnectFourException("Can't play, game is over!")

    def _update_game(self, column_number):
        self._update_board_with_move_on(self._current_player, column_number)
        self._update_if_was_won()
        self._update_current_player()

    def _update_board_with_move_on(self, player_number, column_number):
        next_free_row_number = self._next_free_row_number_by_column[column_number]
        self._board[column_number][next_free_row_number] = player_number
        self._next_free_row_number_by_column[column_number] = next_free_row_number + 1

    def _update_if_was_won(self):
        horizontal_winner = self._board_winner(range(self.width - 3), range(self.height), 1, 0)
        vertical_winner = self._board_winner(range(self.width), range(self.height - 3), 0, 1)
        main_diagonal_winner = self._board_winner(range(self.width - 3), range(self.height - 3), 1, 1)
        anti_diagonal_winner = self._board_winner(range(3, self._width), range(self.height - 3), -1, 1)
        potential_winners = [horizontal_winner, vertical_winner, main_diagonal_winner, anti_diagonal_winner]
        if any(potential_winners):
            self._was_won = True
            self._winner = [winner for winner in potential_winners if winner is not None][0]
            self._is_over = True

    def _board_winner(self, x_range, y_range, x_increment, y_increment):
        for x, y in itertools.product(x_range, y_range):
            line = [self._board[x + i * x_increment][y + i * y_increment] for i in range(4)]
            all_elements_in_line_are_equal = len(set(line)) == 1
            if line[0] != 0 and all_elements_in_line_are_equal:
                return self._board[x][y]
        return None

    def _update_current_player(self):
        self._current_player = 1 if self.current_player == 2 else 2

    def _board_is_full(self):
        return all([self._board[x][y] for (x, y) in list(itertools.product(range(self.width), range(self.height)))])

    def print_board_state(self):
        return '\n'.join([' '.join([str(self._board[x][y]) for x in range(self.width)]) for y in reversed(range(self.height))])


class ConnectFourException(Exception):
    pass

