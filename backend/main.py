from typing import List
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pickleshare import PickleShareDB
from ConnectionManager import ConnectionManager
from models.ConnectFourGame import ConnectFourGame

app = FastAPI()
gameRepository = PickleShareDB('./games_db')
gameId = 'game1'
savedGame = gameRepository.get(gameId)
if not savedGame:
    gameRepository[gameId] = ConnectFourGame(7, 6)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/games/{player_id}")
def get_board(player_id: int):
    if player_id not in [1, 2]:
        raise HTTPException(status_code=404, detail="Player not found")
    player1_board = gameRepository[gameId].board
    board = player1_board if player_id == 1 else [list(reversed(row)) for row in player1_board]
    return {"board": board}


@app.get("/games/{player_id}/drops/{column_number}")
def drop_checker(player_id: int, column_number: int):
    game = gameRepository[gameId]
    if game.current_player == player_id:
        game.drop_checker_on_column(column_number)
        gameRepository[gameId] = game
        return {"message": "successful move"}
    else:
        return {"error": f"it's not {player_id}'s turn"}


@app.get("/reset")
def reset_game():
    gameRepository[gameId] = ConnectFourGame(7, 6)
    return {"message": "game restarted OK"}


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await connectionManager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await connectionManager.send_personal_message(f"You wrote: {data}", websocket)
            await connectionManager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        connectionManager.disconnect(websocket)
        await connectionManager.broadcast(f"Client #{client_id} left the chat")
