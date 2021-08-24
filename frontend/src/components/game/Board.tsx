import React, { useState } from "react";
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

function Board({ width, height, playerNumber, playerId, gameState }:
  {
    width: number, height: number, playerNumber: number, playerId: string, gameState: GameState
  }) {
  const [localGameState, setLocalGameState] = useState(gameState)
  return (
    <div className="board">
      {[0, 1, 2, 3, 4, 5, 6].map(i => {
        return (<div key={i * 7 + 1000 * 6}>
          <ColumnSelector columnSelectorStatus={gameState.availableColumns.includes(i) ?
            ColumnSelectorStatus.AVAILABLE :
            ColumnSelectorStatus.FULL} playerNumber={playerNumber} playerId={playerId} columnNumber={i} plays={localGameState.plays && !localGameState.isOver} onAvailableClickFunction={() => {
              setLocalGameState((localState) => {
                const freeRow = [5, 4, 3, 2, 1, 0].find(row => localState.board[row][i] === 0);
                if (freeRow !== undefined) {
                  localState.board[freeRow][i] = playerNumber;
                  localState.plays = false;
                }
                let newLocalGameStateCopy: GameState = {
                  board: localState.board,
                  plays: localState.plays,
                  availableColumns: localState.availableColumns,
                  isOver: localState.isOver,
                  wasWon: localState.wasWon,
                  winner: localState.winner,
                  wasTied: localState.wasTied
                };
                return newLocalGameStateCopy;
              })
            }} />
        </div>)
      })}
      <div className="clear" />
      {
        localGameState.board.map((row, rowNumber) => {
          return row.map((cell, columnNumber) => {
            return <div key={columnNumber * width + rowNumber * height}>
              <Cell cellStatus={getCellStatus(cell)} />
              {(row.length - 1 === columnNumber) ? <div className="clear" /> : ""}
            </div>
          })
        })}
      {gameState && !gameState.isOver && (gameState.plays ? <p> It's your turn! </p> : <p> It's opponent's turn... </p>)}
    </div>
  );
}

export default Board;