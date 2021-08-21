from fastapi import FastAPI, HTTPException
from pickleshare import PickleShareDB
from models.ConnectFourGame import ConnectFourGame
import json


app = FastAPI()
gameRepository = PickleShareDB('./games_db')
gameId = 'game1'
savedGame = gameRepository.get(gameId)
if not savedGame:
    gameRepository[gameId] = ConnectFourGame(7, 6)


@app.get("/games/{player_id}")
def get_board(player_id: int):
    if player_id not in [1, 2]:
        raise HTTPException(status_code=404, detail="Player not found")
    player1_board = gameRepository[gameId].board
    board = player1_board if player_id == 1 else [list(reversed(row)) for row in player1_board]
    return json.dumps({"board": board})


@app.get("/games/{player_id}/drops/{column_number}")
def drop_checker(player_id: int, column_number: int):
    game = gameRepository[gameId]
    if game.current_player == player_id:
        game.drop_checker_on_column(column_number)
        gameRepository[gameId] = game
        return json.dumps({"message": "successful move"})
    else:
        return json.dumps({"error": f"it's not {player_id}'s turn"})


@app.get("/reset")
def reset_game():
    gameRepository[gameId] = ConnectFourGame(7, 6)
    return json.dumps({"message": "game restarted OK"})
