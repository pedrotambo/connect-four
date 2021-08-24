import React from "react";
import Cell from './Cell'
import { CellStatus } from './Cell'
import ColumnSelector from './ColumnSelector'
import { ColumnSelectorStatus } from './ColumnSelector'
import './styles.css'
import GameState from "./GameState";

const getCellStatus = (cellValue: CellStatus) => {
  switch (cellValue) {
    case 0:
      return CellStatus.EMPTY;
    case 1:
      return CellStatus.PLAYER1;
    case 2:
      return CellStatus.PLAYER2;
    default:
      return CellStatus.EMPTY;
  }
}

function Board({ width, height, playerNumber, playerId, gameState, refetchGameState }:
  {
    width: number, height: number, playerNumber: number, playerId: string, gameState: GameState, refetchGameState: () => any
  }) {
  return (
    <div className="board">
      {[0, 1, 2, 3, 4, 5, 6].map(i => {
        return (<div key={i * 7 + 1000 * 6}>
          <ColumnSelector columnSelectorStatus={gameState.availableColumns.includes(i) ?
            ColumnSelectorStatus.AVAILABLE :
            ColumnSelectorStatus.FULL} playerNumber={playerNumber} playerId={playerId} columnNumber={i} nextFreeRow={[5, 4, 3, 2, 1, 0].find(row => gameState.board[row][i] === 0) || -1}
            plays={gameState.plays && !gameState.isOver} onAvailableClickFunction={() => {
              refetchGameState()
            }} />
        </div>)
      })}
      <div className="clear" />
      {
        gameState.board.map((row, rowNumber) => {
          return row.map((cell, columnNumber) => {
            return <div key={columnNumber * width + rowNumber * height}>
              <Cell cellStatus={getCellStatus(cell)} />
              {(row.length - 1 === columnNumber) ? <div className="clear" /> : ""}
            </div>
          })
        })}
    </div>
  );
}

export default Board;