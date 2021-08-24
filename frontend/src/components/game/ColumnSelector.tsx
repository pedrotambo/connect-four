import React from "react";
import ConnectFourClient from '../../api/ConnectFourClient'


export enum ColumnSelectorStatus {
    AVAILABLE,
    FULL
}

function ColumnSelector({ playerNumber, playerId, columnNumber, columnSelectorStatus, onAvailableClickFunction, plays }:
    {
        playerNumber: number,
        playerId: string,
        columnNumber: number,
        onAvailableClickFunction: () => any,
        columnSelectorStatus: ColumnSelectorStatus,
        plays: boolean
    }) {
    return (
        <div className="column-selector">
            {columnSelectorStatus === ColumnSelectorStatus.AVAILABLE ?
                <button disabled={!plays} className="column-selector-text" onClick={() => {
                    ConnectFourClient.dropChecker(playerId, columnNumber).then(_ => onAvailableClickFunction());
                }}>
                    {playerNumber === 1 ? "🔵" : "🔴"}
                </button> :
                <button disabled={!plays} className="column-selector-text" onClick={() => alert("Column is full! Please choose another column")}>
                    {"✖"}
                </button>

            }
        </div>
    )
}

export default ColumnSelector;