from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pickleshare import PickleShareDB
from models.connect_four_game import ConnectFourGame
from models.connect_four_random_ai_player import ConnectFourRandomAIPlayer


app = FastAPI()
game_repository = PickleShareDB('./games_db')
multiplayer_game_id = 'multiPlayerGame'
single_player_game_id = 'singlePlayerGame'
player_1_id = "1"
player_2_id = "2"
single_player_id = "3"
ai_player_id = 'ai'
multi_player_saved_game = game_repository.get(multiplayer_game_id)
if not multi_player_saved_game:
    game_repository[multiplayer_game_id] = ConnectFourGame(7, 6, player_1_id, player_2_id)
single_player_saved_game = game_repository.get(single_player_game_id)
if not single_player_saved_game:
    game_repository[single_player_game_id] = ConnectFourGame(7, 6, single_player_id, ai_player_id)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/games/{player_id}")
def get_board(player_id: str):
    if player_id not in [player_1_id, player_2_id, single_player_id]:
        raise HTTPException(status_code=404, detail="Player not found")
    game = game_repository[multiplayer_game_id if player_id in [player_1_id, player_2_id] else single_player_game_id]
    return {"board": game.board(player_id),
            "plays": True if game.current_player == player_id else False,
            "available_columns": game.available_column_numbers(player_id),
            "is_over": game.is_over,
            "was_won": game.was_won,
            "winner": game.winner,
            "was_tied": game.was_tied}


@app.get("/games/{player_id}/drops/{column_number}")
def drop_checker(player_id: str, column_number: int):
    game_id = multiplayer_game_id if player_id in [player_1_id, player_2_id] else single_player_game_id
    game = game_repository[game_id]
    if game.current_player == player_id:
        game.drop_checker_on_column(column_number)
        if game_id == single_player_game_id and not game.is_over:
            ConnectFourRandomAIPlayer(ai_player_id, game).play()
        game_repository[game_id] = game
        return {"message": "successful move"}
    else:
        return {"error": f"it's not {player_id}'s turn"}


@app.get("/reset/{game_id}")
def reset_game(game_id: str):
    game_repository[game_id] = ConnectFourGame(7, 6, player_1_id, player_2_id) \
        if game_id == multiplayer_game_id else ConnectFourGame(7, 6, single_player_id, ai_player_id)
    return {"message": "game restarted OK"}

