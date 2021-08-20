import pytest
from models.ConnectFourGame import ConnectFourGame, ConnectFourException


def test_board_is_created_with_correct_dimensions():
    game = ConnectFourGame(7, 6)
    assert game.width == 7, "Wrong width"
    assert game.height == 6, "Wrong height"


def test_cant_put_in_column_bigger_or_equal_than_width():
    game = ConnectFourGame(7, 6)
    with pytest.raises(ConnectFourException) as ex:
        game.put_on(7)
    assert (str(ex.value)) == "Can't play on column bigger or equal than the width, or less than 0."


def test_cant_put_in_column_smaller_than_0():
    game = ConnectFourGame(7, 6)
    with pytest.raises(ConnectFourException) as ex:
        game.put_on(-1)
    assert (str(ex.value)) == "Can't play on column bigger or equal than the width, or less than 0."


def test_starts_playing_1():
    game = ConnectFourGame(7, 6)
    assert game.current_player == 1


def test_current_player_is_2_after_player_1():
    game = ConnectFourGame(7, 6)
    game.put_on(5)
    assert game.current_player == 2


def test_plays_1_after_2():
    game = ConnectFourGame(7, 6)
    first_turn_player = game.current_player
    game.put_on(5)
    second_turn_player = game.current_player
    game.put_on(6)
    assert first_turn_player == 1
    assert second_turn_player == 2
    assert game.current_player == 1


def test_cant_put_more_discs_in_same_column_than_board_height():
    height = 7
    game = ConnectFourGame(6, height)
    column_number = 0
    with pytest.raises(ConnectFourException) as ex:
        for i in range(height + 1):
            game.put_on(column_number)
    assert (str(ex.value)) == f'Column {column_number} is full.'


def test_player_1_wins_horizontally_at_the_beginning_of_first_row():
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    2 2 2 0 0 0 0
    1 1 1 1 0 0 0
    """
    game = ConnectFourGame(7, 6)
    [game.put_on(c) for c in [0, 0, 1, 1, 2, 2, 3]]
    assert game.was_won
    assert game.winner == 1
    assert game.is_over
    assert game.print_board_state() == """\
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
2 2 2 0 0 0 0
1 1 1 1 0 0 0"""


def test_player_1_wins_horizontally_at_the_end_of_first_row():
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    2 0 0 0 0 0 0
    1 2 2 0 0 0 0
    1 2 2 1 1 1 1
    """
    game = ConnectFourGame(7, 6)
    [game.put_on(c) for c in [0, 1, 0, 1, 3, 0, 4, 2, 5, 2, 6]]
    assert game.was_won
    assert game.winner == 1
    assert game.is_over
    assert game.print_board_state() == """\
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
2 0 0 0 0 0 0
1 2 2 0 0 0 0
1 2 2 1 1 1 1"""


def test_player_1_wins_vertically_at_the_beginning_of_first_column():
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    1 0 0 0 0 0 0
    1 2 0 0 0 0 0
    1 2 0 0 0 0 0
    1 2 0 0 0 0 0
    """
    game = ConnectFourGame(7, 6)
    [game.put_on(c) for c in [0, 1, 0, 1, 0, 1, 0]]
    assert game.was_won
    assert game.winner == 1
    assert game.is_over
    assert game.print_board_state() == """\
0 0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0
1 2 0 0 0 0 0
1 2 0 0 0 0 0
1 2 0 0 0 0 0"""


def test_player_1_wins_vertically_at_end_of_first_column():
    """
    Board final state is
    1 2 0 0 0 0 0
    1 2 0 0 0 0 0
    1 2 0 0 0 0 0
    1 1 0 0 0 0 0
    2 1 0 0 0 0 0
    2 1 2 0 0 0 0
    """
    game = ConnectFourGame(7, 6)
    [game.put_on(c) for c in [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 2, 0]]
    assert game.was_won
    assert game.winner == 1
    assert game.print_board_state() == """\
1 2 0 0 0 0 0
1 2 0 0 0 0 0
1 2 0 0 0 0 0
1 1 0 0 0 0 0
2 1 0 0 0 0 0
2 1 2 0 0 0 0"""


def test_player_1_wins_diagonally_at_beginning_of_the_main_diagonal():
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 1 0 0 0
    0 0 1 1 0 0 0
    2 1 2 2 0 0 0
    1 2 2 1 0 0 0
    """
    game = ConnectFourGame(7, 6)
    [game.put_on(c) for c in [3, 3, 3, 2, 3, 2, 0, 1, 1, 0, 2]]
    assert game.was_won
    assert game.winner == 1
    assert game.is_over
    assert game.print_board_state() == """\
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 1 1 0 0 0
2 1 2 2 0 0 0
1 2 2 1 0 0 0"""


def test_player_1_wins_diagonally_at_end_of_the_main_diagonal():
    """
    Board final state is
    0 0 0 0 0 2 1
    0 0 0 0 0 1 1
    0 0 0 0 1 2 2
    0 0 0 1 2 2 2
    0 0 0 2 1 1 1
    0 0 0 1 2 2 1
    """
    game = ConnectFourGame(7, 6)
    [game.put_on(c) for c in [3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 5, 6, 6, 5, 6, 6, 5, 6]]
    assert game.was_won
    assert game.winner == 1
    assert game.is_over
    assert game.print_board_state() == """\
0 0 0 0 0 2 1
0 0 0 0 0 1 1
0 0 0 0 1 2 2
0 0 0 1 2 2 2
0 0 0 2 1 1 1
0 0 0 1 2 2 1"""
