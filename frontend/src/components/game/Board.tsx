import React from "react";
import Cell from './Cell'
import {CellStatus} from './Cell'

const getCellStatus = (cellValue: CellStatus) => {
    switch(cellValue) {
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

function Board({width, height, boardData}: {width: number, height: number, boardData: number[][]}) {
    return (
        <div className="board">
            {boardData.map((row, rowNumber) => {
                return row.map((cell, columnNumber) => {
                    return <div key={columnNumber * width + rowNumber * height}>
                        <Cell cellStatus={getCellStatus(cell)}/>
                        {(row.length - 1 === columnNumber) ? <div className="clear" /> : ""}
                    </div>
                })
            })}
        </div>
    );
}

export default Board;