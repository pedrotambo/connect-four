import pytest
from models.connect_four_game import ConnectFourGame, ConnectFourException


@pytest.fixture
def game():
    return ConnectFourGame(7, 6, "player1", "player2")


def test_board_is_created_with_correct_dimensions(game):
    assert game.width == 7, "Wrong width"
    assert game.height == 6, "Wrong height"


def test_cant_put_in_column_bigger_or_equal_than_width(game):
    with pytest.raises(ConnectFourException) as ex:
        game.drop_checker_on_column(7)
    assert (str(ex.value)) == "Can't play on column bigger or equal than the width, or less than 0."


def test_cant_put_in_column_smaller_than_0(game):
    with pytest.raises(ConnectFourException) as ex:
        game.drop_checker_on_column(-1)
    assert (str(ex.value)) == "Can't play on column bigger or equal than the width, or less than 0."


def test_cant_get_board_of_non_player(game):
    game = ConnectFourGame(7, 6, "player1", "player2")

    with pytest.raises(ConnectFourException) as ex:
        game.board("non-playing player")
    assert (str(ex.value)) == "Can't get board of non-playing player."


def test_starts_playing_1(game):
    assert game.current_player == "player1"


def test_current_player_is_2_after_player_1(game):
    game.drop_checker_on_column(5)
    assert game.current_player == "player2"


def test_plays_1_after_2(game):
    first_turn_player = game.current_player
    game.drop_checker_on_column(5)
    second_turn_player = game.current_player
    game.drop_checker_on_column(6)
    assert first_turn_player == "player1"
    assert second_turn_player == "player2"
    assert game.current_player == "player1"


def test_cant_put_more_discs_in_same_column_than_board_height():
    game = ConnectFourGame(7, 6, "player1", "player2")
    column_number = 0
    [game.drop_checker_on_column(c) for c in [0, 6, 0, 6, 0, 6]]
    with pytest.raises(ConnectFourException) as ex:
        game.drop_checker_on_column(column_number)
    assert (str(ex.value)) == f'Column {column_number} is full.'


def test_player_1_wins_horizontally_at_the_beginning_of_first_row(game):
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    2 2 2 0 0 0 0
    1 1 1 1 0 0 0
    """
    [game.drop_checker_on_column(c) for c in [0, 6, 1, 5, 2, 4, 3]]
    assert game.was_won
    assert game.winner == "player1"
    assert game.is_over
    assert game.board("player1") == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0]
    ]


def test_player_1_wins_horizontally_at_the_end_of_first_row(game):
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    2 0 0 0 0 0 0
    1 2 2 0 0 0 0
    1 2 2 1 1 1 1
    """
    [game.drop_checker_on_column(c) for c in [0, 5, 0, 5, 3, 6, 4, 4, 5, 4, 6]]
    assert game.was_won
    assert game.winner == "player1"
    assert game.is_over
    assert game.board("player1") == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0],
        [1, 2, 2, 0, 0, 0, 0],
        [1, 2, 2, 1, 1, 1, 1]
    ]


def test_player_1_wins_vertically_at_the_beginning_of_first_column(game):
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    1 0 0 0 0 0 0
    1 2 0 0 0 0 0
    1 2 0 0 0 0 0
    1 2 0 0 0 0 0
    """
    [game.drop_checker_on_column(c) for c in [0, 5, 0, 5, 0, 5, 0]]
    assert game.was_won
    assert game.winner == "player1"
    assert game.is_over
    assert game.board("player1") == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 2, 0, 0, 0, 0, 0],
        [1, 2, 0, 0, 0, 0, 0],
        [1, 2, 0, 0, 0, 0, 0]
    ]


def test_player_1_wins_vertically_at_end_of_first_column(game):
    """
    Board final state is
    1 2 0 0 0 0 0
    1 2 0 0 0 0 0
    1 2 0 0 0 0 0
    1 1 0 0 0 0 0
    2 1 0 0 0 0 0
    2 1 2 0 0 0 0
    """
    [game.drop_checker_on_column(c) for c in [1, 6, 1, 6, 1, 5, 0, 5, 0, 5, 0, 4, 0]]
    assert game.was_won
    assert game.winner == "player1"
    assert game.board("player1") == [
        [1, 2, 0, 0, 0, 0, 0],
        [1, 2, 0, 0, 0, 0, 0],
        [1, 2, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0],
        [2, 1, 2, 0, 0, 0, 0]
    ]


def test_player_1_wins_diagonally_at_beginning_of_the_main_diagonal(game):
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 1 0 0 0
    0 0 1 1 0 0 0
    2 1 2 2 0 0 0
    1 2 2 1 0 0 0
    """
    [game.drop_checker_on_column(c) for c in [3, 3, 3, 4, 3, 4, 0, 5, 1, 6, 2]]
    assert game.was_won
    assert game.winner == "player1"
    assert game.is_over
    assert game.board("player1") == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [2, 1, 2, 2, 0, 0, 0],
        [1, 2, 2, 1, 0, 0, 0]
    ]


def test_player_1_wins_diagonally_at_end_of_the_main_diagonal(game):
    """
    Board final state is
    0 0 0 0 0 2 1
    0 0 0 0 0 1 1
    0 0 0 0 1 2 2
    0 0 0 1 2 2 2
    0 0 0 2 1 1 1
    0 0 0 1 2 2 1
    """
    [game.drop_checker_on_column(c) for c in [3, 3, 3, 2, 4, 2, 4, 1, 5, 1, 6, 1, 6, 0, 5, 0, 6, 1, 6]]
    assert game.was_won
    assert game.winner == "player1"
    assert game.is_over
    assert game.board("player1") == [
        [0, 0, 0, 0, 0, 2, 1],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1, 2, 2],
        [0, 0, 0, 1, 2, 2, 2],
        [0, 0, 0, 2, 1, 1, 1],
        [0, 0, 0, 1, 2, 2, 1]
    ]


def test_player_1_wins_diagonally_at_the_beginning_of_the_anti_diagonal(game):
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 1 0 0 0
    0 0 0 2 1 0 0
    0 0 0 1 1 1 2
    0 0 0 2 2 2 1
    """
    [game.drop_checker_on_column(c) for c in [6, 1, 5, 2, 4, 0, 4, 3, 3, 3, 3]]
    assert game.was_won
    assert game.winner == "player1"
    assert game.is_over
    assert game.board("player1") == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 2],
        [0, 0, 0, 2, 2, 2, 1]
    ]


def test_cant_play_after_game_is_over(game):
    """
    Board final state is
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    2 2 2 0 0 0 0
    1 1 1 1 0 0 0
    """
    [game.drop_checker_on_column(c) for c in [0, 0, 1, 1, 2, 2, 3]]
    assert game.was_won
    assert game.winner == "player1"
    assert game.is_over
    with pytest.raises(ConnectFourException) as ex:
        game.drop_checker_on_column(4)
    assert (str(ex.value)) == "Can't play, game is over!"


def test_game_was_tied(game):
    """
    Board final state is
    2 2 2 1 2 2 2
    1 1 1 2 1 1 1
    2 2 2 1 2 2 2
    1 1 1 2 1 1 1
    2 2 2 1 2 2 2
    1 1 1 2 1 1 1
    """
    # [game.drop_checker_on_column(c) for c in [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 4, 3, 3,
    #                                           4, 5, 3, 3, 3, 3, 5, 6, 6, 4, 4, 5, 5, 6, 6, 4, 4, 5, 5, 6, 6]]
    # moves = [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2, 4, 3, 3,
    #  4, 5, 3, 3, 3, 3, 5, 6, 6, 4, 4, 5, 5, 6, 6, 4, 4, 5, 5, 6, 6]
    ms = [0, 6, 1, 5, 2, 4, 0, 6, 1, 5, 2, 4, 0, 6, 1, 5, 2, 4, 4, 3, 3, 2, 5, 3, 3, 3, 3, 1, 6, 0, 4, 2, 5, 1, 6, 0, 4, 2, 5, 1, 6, 0]
    [game.drop_checker_on_column(c) for c in ms]
    # translate = [ col if (i % 2 ) == 0 else - col + 7 - 1 for (i, col) in enumerate(moves) ]
    assert game.is_over
    assert game.was_tied
    assert not game.was_won
    assert game.winner is None
    assert game.board("player1") == [
        [2, 2, 2, 1, 2, 2, 2],
        [1, 1, 1, 2, 1, 1, 1],
        [2, 2, 2, 1, 2, 2, 2],
        [1, 1, 1, 2, 1, 1, 1],
        [2, 2, 2, 1, 2, 2, 2],
        [1, 1, 1, 2, 1, 1, 1]
    ]


def test_all_columns_are_available_when_empty_game(game):
    assert game.available_column_numbers == list(range(game.width))
    assert game.available_column_numbers2(game.player_1_name) == list(range(game.width))
    assert game.available_column_numbers2(game.player_2_name) == list(range(game.width))


def test_cant_ask_available_columns_for_non_playing_player(game):
    no_player = "no_player"
    assert game.player_1_name != no_player
    assert game.player_2_name != no_player
    with pytest.raises(ConnectFourException) as ex:
        game.available_column_numbers2(no_player)
    assert (str(ex.value)) == "Can't get available moves of non-playing player."


def test_column_is_not_available_when_it_is_full(game):
    full_column_number = 0
    [game.drop_checker_on_column(c) for c in [0, 6, 0, 6, 0, 6]]
    assert full_column_number not in game.available_column_numbers
    for available_column_number in range(1, game.height):
        assert available_column_number in game.available_column_numbers
