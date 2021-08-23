import React from "react";


export enum CellStatus {
    EMPTY,
    PLAYER1,
    PLAYER2
}

const getCell = (cellStatus: CellStatus) => {
    switch(cellStatus) {
        case CellStatus.EMPTY:
            return "";
        case CellStatus.PLAYER1:
            return "🔵";
        case CellStatus.PLAYER2:
            return "🔴";
    }
}

function Cell({cellStatus}: {cellStatus: CellStatus}) {
    return (
        <div className="cell">
            {getCell(cellStatus)}
        </div>
    )
}

export default Cell;