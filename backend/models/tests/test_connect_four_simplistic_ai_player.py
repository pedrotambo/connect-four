import pytest
from models.connect_four_game import ConnectFourGame
from models.connect_four_simplistic_ai_player import ConnectFourSimplisticAIPlayer


def test_ai_player_selects_horizontal_winner_move(mocker):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [2, 2, 2, 1, 0, 0, 0],
    ]
    board2 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 2, 2, 2],
    ]
    ai_player = ConnectFourSimplisticAIPlayer('basic', mocker.MagicMock(player_1_name="basic", player_2_name="test", is_over=False, current_player="basic"))
    assert ai_player.winner_moves(board) == [3]
    assert ai_player.winner_moves(board2) == [3]


def test_ai_player_selects_vertical_winner_move(mocker):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 2, 0, 0],
    ]
    game_mock = mocker.MagicMock(player_1_name="basic", player_2_name="test", is_over=False, current_player="basic")
    game_mock.board = mocker.MagicMock(return_value=board)
    ai_player = ConnectFourSimplisticAIPlayer('basic', game_mock)
    assert ai_player.winner_moves(board) == [4]


def test_ai_player_selects_main_diagonal_winner_move(mocker):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 2, 0],
        [0, 0, 0, 1, 2, 2, 1],
        [0, 0, 1, 2, 2, 2, 1],
    ]
    board2 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 2, 0],
        [0, 0, 0, 1, 2, 2, 1],
        [0, 0, 0, 2, 2, 2, 1],
    ]
    game_mock = mocker.MagicMock(player_1_name="basic", player_2_name="test", is_over=False, current_player="basic")
    game_mock.board = mocker.MagicMock(return_value=board)
    ai_player = ConnectFourSimplisticAIPlayer('basic', game_mock)
    assert ai_player.winner_moves(board) == [5]
    assert ai_player.winner_moves(board2) == [2]


def test_ai_player_selects_anti_main_diagonal_winner_move(mocker):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 1, 0, 0, 0, 0],
        [1, 2, 2, 1, 0, 0, 0],
        [1, 2, 2, 2, 1, 0, 0]
    ]
    board2 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0],
        [0, 2, 1, 0, 0, 0, 0],
        [1, 2, 2, 1, 0, 0, 0],
        [1, 2, 2, 2, 0, 0, 0]
    ]
    game_mock = mocker.MagicMock(player_1_name="basic", player_2_name="test", is_over=False, current_player="basic")
    game_mock.board = mocker.MagicMock(return_value=board)
    ai_player = ConnectFourSimplisticAIPlayer('basic', game_mock)
    assert ai_player.winner_moves(board) == [1]
    assert ai_player.winner_moves(board2) == [4]


def test_ai_player_selects_horizontal_three_liner_move(mocker):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [2, 2, 2, 1, 0, 0, 0],
    ]
    board2 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 2, 2, 2],
    ]
    ai_player = ConnectFourSimplisticAIPlayer('basic', mocker.MagicMock(player_1_name="basic", player_2_name="test", is_over=False, current_player="basic"))
    assert ai_player.three_liner_moves(board) == [2]
    assert ai_player.three_liner_moves(board2) == [4]


def test_ai_player_selects_vertical_three_liner_move(mocker):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
    ]
    ai_player = ConnectFourSimplisticAIPlayer('basic', mocker.MagicMock(player_1_name="basic", player_2_name="test", is_over=False, current_player="basic"))
    assert ai_player.three_liner_moves(board) == [4]


def test_ai_player_selects_main_diagonal_three_liner_move(mocker):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 2, 0],
        [0, 0, 0, 1, 2, 2, 0],
    ]
    ai_player = ConnectFourSimplisticAIPlayer('basic', mocker.MagicMock(player_1_name="basic", player_2_name="test", is_over=False, current_player="basic"))
    assert ai_player.three_liner_moves(board) == [5]


def test_ai_player_selects_anti_main_diagonal_three_liner_move(mocker):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 0, 0, 0, 0],
        [0, 2, 2, 1, 0, 0, 0]
    ]
    ai_player = ConnectFourSimplisticAIPlayer('basic', mocker.MagicMock(player_1_name="basic", player_2_name="test", is_over=False, current_player="basic"))
    assert ai_player.three_liner_moves(board) == [1]