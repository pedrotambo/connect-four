from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pickleshare import PickleShareDB
from models.connect_four_game import ConnectFourGame

app = FastAPI()
game_repository = PickleShareDB('./games_db')
multiplayer_game_id = 'game1'
player_1_id = "1"
player_2_id = "2"
savedGame = game_repository.get(multiplayer_game_id)
if not savedGame:
    game_repository[multiplayer_game_id] = ConnectFourGame(7, 6, player_1_id, player_2_id)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/games/{player_id}")
def get_board(player_id: str):
    if player_id not in [player_1_id, player_2_id]:
        raise HTTPException(status_code=404, detail="Player not found")
    game = game_repository[multiplayer_game_id]
    return {"board": game.board(player_id), "plays": True if game.current_player == player_id else False}


@app.get("/games/{player_id}/drops/{column_number}")
def drop_checker(player_id: str, column_number: int):
    game = game_repository[multiplayer_game_id]
    if game.current_player == player_id:
        game.drop_checker_on_column(column_number)
        game_repository[multiplayer_game_id] = game
        return {"message": "successful move"}
    else:
        return {"error": f"it's not {player_id}'s turn"}


@app.get("/reset/{game_id}")
def reset_game(game_id: str):
    game_repository[game_id] = ConnectFourGame(7, 6, player_1_id, player_2_id)
    return {"message": "game restarted OK"}

