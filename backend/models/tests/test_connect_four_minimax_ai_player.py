# import pytest
# from models.connect_four_game import ConnectFourGame
# from models.connect_four_minimax_ai_player import ConnectFourMiniMaxAIPlayer
#
#
# def test_ai_player_cant_play_in_a_game_where_it_is_not_a_player(mocker):
#     board = [
#         [1, 0, 0, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0, 0, 0],
#         [2, 0, 0, 0, 0, 0, 0],
#         [2, 0, 0, 0, 0, 0, 0],
#         [2, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 0, 0, 0],
#     ]
#     game_mock = mocker.MagicMock(player_1_name="minimax", player_2_name="test", is_over=False, current_player="minimax")
#     game_mock.board = mocker.MagicMock(return_value=board)
#     ai_player = ConnectFourMiniMaxAIPlayer('minimax', game_mock)
#     ai_player.play()
