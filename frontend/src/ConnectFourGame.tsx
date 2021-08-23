import React from 'react';
import './ConnectFourGame.css';
import Board from './components/gameboard/Board'
import { useQuery } from 'react-query'
import ConnectFourClient from './api/ConnectFourClient'

function ConnectFourGame() {
  const { isLoading, isError, data, error } = useQuery('player1_board', () => ConnectFourClient.player_board(1), {refetchInterval: 5000});
  if (isLoading) {
    console.log('making query')
  }
  return (
    <div className="ConnectFourGame">
      <header className="ConnectFourGame-header">
        <div className="game-info">
          <span className="info"> Welcome to ConnectFour! </span>
        </div>
      </header>
      <div>
        {isError && <p> There was an error loading the board! Error: {error} </p>}
        {!isLoading && !isError && <Board width={7} height={6} boardData={data.board}></Board>}
      </div>
    </div>
  );
}

export default ConnectFourGame;