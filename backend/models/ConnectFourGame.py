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
        self._was_tied = False
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
    def was_tied(self):
        return self._was_tied

    @property
    def winner(self):
        return self._winner if self.is_over else None

    @property
    def is_over(self):
        return self.was_won or self.was_tied

    def put_on(self, column_number):
        # validate move
        if not 0 <= column_number < self._width:
            raise ConnectFourException("Can't play on column bigger or equal than the width, or less than 0.")

        if self._next_free_row_number_by_column[column_number] >= self._height:
            raise ConnectFourException(f'Column {column_number} is full.')

        self._update_board_with_move_on(self._current_player, column_number)
        self._update_if_was_won()
        self._update_current_player()

    def _update_board_with_move_on(self, player_number, column_number):
        next_free_row_number = self._next_free_row_number_by_column[column_number]
        # self._board[column_number][next_free_row_number] = self._current_player
        self._board[column_number][next_free_row_number] = player_number
        self._next_free_row_number_by_column[column_number] = next_free_row_number + 1

    def _update_if_was_won(self):
        # check if current player won horizontally
        for x, y in itertools.product(range(self.width - 3), range(self.height)):
            if self._board[x][y] != 0 and self._board[x][y] == self._board[x + 1][y] == self._board[x + 2][y] == self._board[x + 3][y]:
                self._was_won = True
                self._winner = self._board[x][y]
                self._is_over = True
                break

        # check if current player won vertically
        for x, y in itertools.product(range(self.width), range(self.height - 3)):
            if self._board[x][y] != 0 and self._board[x][y] == self._board[x][y + 1] == self._board[x][y + 2] == self._board[x][y + 3]:
                self._was_won = True
                self._winner = self._board[x][y]
                self._is_over = True
                break

        # check if current player won bottom-top diagonally
        for x, y in itertools.product(range(self.width - 3), range(self.height - 3)):
            if self._board[x][y] != 0 and self._board[x][y] == self._board[x + 1][y + 1] == self._board[x + 2][y + 2] == self._board[x + 3][y + 3]:
                self._was_won = True
                self._winner = self._board[x][y]
                self._is_over = True
                break

    def _update_current_player(self):
        self._current_player = 1 if self.current_player == 2 else 2

    def print_board_state(self):
        return '\n'.join([' '.join([str(self._board[x][y]) for x in range(self.width)]) for y in reversed(range(self.height))])


class ConnectFourException(Exception):
    pass

