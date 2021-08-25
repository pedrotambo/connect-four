import React from 'react';
import './styles.css';
import Board from './Board'
import { useQuery } from 'react-query'
import ConnectFourClient from '../../api/ConnectFourClient'
import GameState from './GameState'

function ConnectFourGame({ playerNumber, playerId, gameId, refetchIntervalMs, singlePlayer }:
  { playerNumber: number, playerId: string, gameId: string, refetchIntervalMs: number, singlePlayer: boolean }) {
  const { isError, data, error, refetch } = useQuery(`player${playerNumber}_board`,
    () => ConnectFourClient.playerBoard(playerId), { refetchInterval: refetchIntervalMs });

  const gameState: GameState | undefined = !data ? undefined : {
    board: data.board,
    plays: data.plays,
    availableColumns: data.available_columns,
    isOver: data.is_over,
    wasWon: data.was_won,
    winner: data.winner,
    wasTied: data.was_tied
  }

  return (
    <div className="ConnectFourGame">
      <header className="ConnectFourGame-header" />
      <div className="ConnectFourGameBody">
        {isError && <p> There was an error loading the board! Error: {error} </p>}
        <div className="clear" />
        {gameState && <Board width={7} height={6} playerId={playerId} gameState={gameState}
          playerNumber={playerNumber} refetchGameState={refetch} ></Board>}
        <br/>
        {gameState && <button onClick={() => ConnectFourClient.resetGame(gameId).then(refetch)}> Reset </button>}
        {gameState && !gameState.isOver && (gameState.plays ? <p> It's your turn! </p> : <p> Waiting for your opponent... </p>)}
        {gameState && gameState.isOver && !gameState.wasTied && (gameState.winner === playerId ? <p> You won! 🥳🎉 </p> : <p> You Lost! 😭 </p>)}
        {gameState && gameState.isOver && gameState.wasTied && <p> It's a tie! </p>}
      </div>
    </div>
  );
}

export default ConnectFourGame;