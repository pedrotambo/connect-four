import React from "react";
import ConnectFourClient from '../../api/ConnectFourClient'


export enum ColumnSelectorStatus {
    AVAILABLE,
    FULL
}

function availableOnClickFunction (playerId: string, columnNumber: number) {
    return () =>  ConnectFourClient.dropChecker(playerId, columnNumber);
};
    

function ColumnSelector({playerNumber, playerId, columnNumber, columnSelectorStatus}: 
    {   playerNumber: number,
        playerId: string,
        columnNumber: number,
        columnSelectorStatus: ColumnSelectorStatus} ) {
    return (
        <div className="column-selector">
            { columnSelectorStatus === ColumnSelectorStatus.AVAILABLE ?
                <button className="column-selector-text" onClick={availableOnClickFunction(playerId, columnNumber)}>
                    {playerNumber === 1 ? "🔵" : "🔴"}
                </button> :
                <button className="column-selector-text" onClick={() => alert("I'm an alert!")}>
                    {"✖"}
                </button>

            }
        </div>
    )
}

export default ColumnSelector;