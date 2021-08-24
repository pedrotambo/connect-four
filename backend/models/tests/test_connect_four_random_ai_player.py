import pytest
from models.connect_four_game import ConnectFourGame, ConnectFourException
from models.connect_four_random_ai_player import ConnectFourRandomAIPlayer


def test_ai_player_cant_play_in_a_game_where_it_is_not_a_player():
    game = ConnectFourGame(7, 6, "player1", "player1")
    with pytest.raises(ValueError) as ex:
        ConnectFourRandomAIPlayer("non_playing_ai_player_name", game)
    assert (str(ex.value)) == "Can't play in a game that i am not a player"


def test_ai_cant_play_if_it_is_not_its_turn():
    ai_name = "random_ai_player"
    game = ConnectFourGame(7, 6, "player1", ai_name)
    ai_player = ConnectFourRandomAIPlayer(ai_name, game)
    assert game.current_player == "player1"
    with pytest.raises(ValueError) as ex:
        ai_player.play()
    assert (str(ex.value)) == "Can't play when it's not my turn or game is over."
    assert game.current_player == "player1"


def test_ai_cant_play_if_game_is_over(mocker):
    game_mock = mocker.MagicMock(player_1_name="ai_name", current_player="ai_name")
    is_true_mock = mocker.PropertyMock(return_value=True)
    type(game_mock).is_over = is_true_mock
    game_mock.drop_checker_on_column = mocker.MagicMock()
    ai_player = ConnectFourRandomAIPlayer("ai_name", game_mock)
    with pytest.raises(ValueError) as ex:
        ai_player.play()
    assert (str(ex.value)) == "Can't play when it's not my turn or game is over."
    assert is_true_mock.called
    assert not game_mock.drop_checker_on_column.called


def test_ai_play_if_it_is_its_turn():
    ai_name = "random_ai_player"
    game = ConnectFourGame(7, 6, "player1", ai_name)
    ai_player = ConnectFourRandomAIPlayer(ai_name, game)
    assert not game.current_player == ai_name
    game.drop_checker_on_column(1)
    assert game.current_player == ai_name
    ai_player.play()
    assert not game.current_player == ai_name


def test_ai_selects_the_only_available_column_number(mocker):
    available_column_number = 4
    game_mock = mocker.MagicMock(player_1_name="ai_name", current_player="ai_name", is_over=False)
    game_mock.available_column_numbers = mocker.MagicMock(return_value=[available_column_number])
    ai_player = ConnectFourRandomAIPlayer("ai_name", game_mock)
    ai_player.play()
    game_mock.drop_checker_on_column.assert_called_once_with(available_column_number)
