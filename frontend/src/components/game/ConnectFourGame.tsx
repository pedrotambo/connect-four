import React from 'react';
import './styles.css';
import Board from './Board'
import { useQuery } from 'react-query'
import ConnectFourClient from '../../api/ConnectFourClient'
import GameState from './GameState'

function ConnectFourGame({ playerNumber, playerId, gameId, refetchIntervalMs }: { playerNumber: number, playerId: string, gameId: string, refetchIntervalMs: number }) {
  const { isLoading, isError, data, error } = useQuery(`player${playerNumber}_board`, () => ConnectFourClient.playerBoard(playerId), { refetchInterval: refetchIntervalMs });
  const a = Math.random() * (0 - 10) + 0;
  let gameState: GameState | undefined = undefined;
  if (isLoading) {
    console.log("Loading...")
  } else {
    gameState = {
      board: data.board,
      plays: data.plays,
      availableColumns: data.available_columns,
      isOver: data.is_over,
      wasWon: data.was_won,
      winner: data.winner,
      wasTied: data.was_tied
    }
  }
  
  return (
    <div className="ConnectFourGame">
      <header className="ConnectFourGame-header" />
      <div className="ConnectFourGameBody">
        {isLoading && <p> ASDF </p>}
        {isError && <p> There was an error loading the board! Error: {error} </p>}
        <div className="clear" />
        {gameState && data && <Board key={a} width={7} height={6} playerId={playerId} gameState={gameState}
          playerNumber={playerNumber} ></Board>}
        {data && data.is_over && !data.was_tied && (data.winner === playerId ? <p> You won! 🥳🎉 </p> : <p> You Lost! 😭 </p>)}
        {data && <button onClick={() => ConnectFourClient.resetGame(gameId)}> Reset </button>}
      </div>
    </div>
  );
}

export default ConnectFourGame;