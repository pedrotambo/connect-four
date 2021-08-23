import React from 'react';
import './styles.css';
import Board from './Board'
import { useQuery } from 'react-query'
import ConnectFourClient from '../../api/ConnectFourClient'

function ConnectFourGame({player_number}: {player_number: number}) {
  const { isLoading, isError, data, error } = useQuery(`player${player_number}_board`, () => ConnectFourClient.player_board(player_number), {refetchInterval: 5000});
  if (isLoading) {
    console.log("Loading...")
  }
  
  return (
    <div className="ConnectFourGame">
      <header className="ConnectFourGame-header"/>
      <div>
        {isError && <p> There was an error loading the board! Error: {error} </p>}
        {data && !isError && <Board width={7} height={6} boardData={data.board}></Board>}
        {data && data.plays && <p> It's your turn! </p>}
        {data && !data.plays && <p> Waiting for the opponent to play... </p>}
      </div>
    </div>
  );
}

export default ConnectFourGame;