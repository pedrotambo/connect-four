import pytest
from models.connect_four_game import ConnectFourGame, ConnectFourException
from models.connect_four_random_ai_player import ConnectFourRandomAIPlayer


def test_ai_player_cant_play_in_a_game_where_it_is_not_a_player():
    game = ConnectFourGame(7, 6, "player1", "player1")
    with pytest.raises(ValueError) as ex:
        ConnectFourRandomAIPlayer("non_playing_ai_player_name", game)
    assert (str(ex.value)) == "Can't play in a game that it's not a player"


def test_ai_doesnt_play_if_it_is_not_its_turn():
    ai_name = "random_ai_player"
    game = ConnectFourGame(7, 6, "player1", ai_name)
    ai_player = ConnectFourRandomAIPlayer(ai_name, game)
    assert game.current_player == "player1"
    ai_player.play()
    assert game.current_player == "player1"


def test_ai_play_if_it_is_its_turn():
    ai_name = "random_ai_player"
    game = ConnectFourGame(7, 6, "player1", ai_name)
    ai_player = ConnectFourRandomAIPlayer(ai_name, game)
    assert not game.current_player == ai_name
    game.drop_checker_on_column(1)
    assert game.current_player == ai_name
    ai_player.play()
    assert not game.current_player == ai_name




