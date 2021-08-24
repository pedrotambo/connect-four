import React from 'react';
import './styles.css';
import Board from './Board'
import { useQuery } from 'react-query'
import ConnectFourClient from '../../api/ConnectFourClient'
import ColumnSelector from './ColumnSelector'
import {ColumnSelectorStatus} from './ColumnSelector'

function ConnectFourGame({playerNumber, playerId}: {playerNumber: number, playerId: string}) {
  const { isLoading, isError, data, error } = useQuery(`player${playerNumber}_board`, () => ConnectFourClient.playerBoard(playerId), {refetchInterval: 300});
  if (isLoading) {
    console.log("Loading...")
  } 
  return (
    <div className="ConnectFourGame">
      <header className="ConnectFourGame-header"/>
      <div>
        {isError && <p> There was an error loading the board! Error: {error} </p>}
        
        {/* {Game is not Over} */}
        {data && !data.is_over && [0,1,2,3,4,5,6].map(i => {
          return (<div key={i * 7 + 1000 * 6} className="asdf">
          <ColumnSelector columnSelectorStatus={data.available_columns.includes(i) ? 
            ColumnSelectorStatus.AVAILABLE : 
            ColumnSelectorStatus.FULL} playerNumber={playerNumber} playerId={playerId} columnNumber={i} />
        </div>)})}
        <div className="clear" />
        {data && !data.is_over && <Board width={7} height={6} boardData={data.board}></Board>}
        {data && !data.is_over && data.plays && <p> It's your turn! </p>}
        {data && !data.is_over && !data.plays && <p> It's opponent's turn... </p>}

        {/* {Game is over} */}
        {data && data.is_over && data.was_won && data.winner === "player1"? <p> Congratulations!</p> : <p> Maybe next time!</p>

        }
      </div>
    </div>
  );
}

export default ConnectFourGame;