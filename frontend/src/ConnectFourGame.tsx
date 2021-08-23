import React from 'react';
import './ConnectFourGame.css';
import Board from './components/gameboard/Board'
import { useQuery } from 'react-query'
import ConnectFourClient from './api/ConnectFourClient'

function ConnectFourGame({player_number}: {player_number: number}) {
  const { isLoading, isError, data, error } = useQuery(`player${player_number}_board`, () => ConnectFourClient.player_board(player_number), {refetchInterval: 5000});
  return (
    <div className="ConnectFourGame">
      <header className="ConnectFourGame-header"/>
      <div>
        {isError && <p> There was an error loading the board! Error: {error} </p>}
        {!isLoading && !isError && <Board width={7} height={6} boardData={data.board}></Board>}
      </div>
    </div>
  );
}

export default ConnectFourGame;