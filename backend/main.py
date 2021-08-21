from fastapi import FastAPI
import json
from models.ConnectFourGame import ConnectFourGame

app = FastAPI()
games = {'game1': ConnectFourGame(7, 6)}


@app.get("/games/{player_id}")
def get_board(player_id: int):
    if player_id in [1, 2]:
        # board = game.board if player_id == 1 else [list(reversed(row)) for row in game.board]
        player1_board = games['game1'].board
        board = player1_board if player_id == 1 else [list(reversed(row)) for row in player1_board]
        return json.dumps({"board": board})
    else:
        return json.dumps({"error": f'player {player_id} doesn\'t exist!'})


@app.get("/games/{player_id}/drops/{column_number}")
def drop_checker(player_id: int, column_number: int):
    game = games['game1']
    if game.current_player == player_id:
        game.drop_checker_on_column(column_number)
        return json.dumps({"status": "success"})
    else:
        return json.dumps({"error": "you can't play, it's not your turn"})


@app.get("/reset")
def reset_game():
    games['game1'] = ConnectFourGame(7, 6)
    return json.dumps({"message": "{game restarted OK}"})