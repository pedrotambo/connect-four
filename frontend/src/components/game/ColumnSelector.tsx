import React, { useState } from "react";
import ConnectFourClient from '../../api/ConnectFourClient'


export enum ColumnSelectorStatus {
    AVAILABLE,
    FULL
}

function ColumnSelector({ playerNumber, playerId, columnNumber, columnSelectorStatus, onAvailableClickFunction, plays, nextFreeRow }:
    {
        playerNumber: number,
        playerId: string,
        columnNumber: number,
        onAvailableClickFunction: () => any,
        columnSelectorStatus: ColumnSelectorStatus,
        plays: boolean,
        nextFreeRow: number
    }) {
    const [isFalling, setIsFalling] = useState(false);
    const onClick = () => {
        setIsFalling(true);
        return ConnectFourClient.dropChecker(playerId, columnNumber).then(_ => onAvailableClickFunction()).then(_ => setIsFalling(false));
    }

    const checkerStyle = {
        transform: isFalling ? `translate(0px,${47 * (nextFreeRow + 1)}px)` : '',
        // transition: isFalling ? 'translate 1s' : 'translate 0s'
    };
    return (
        <div className="column-selector">
            {columnSelectorStatus === ColumnSelectorStatus.AVAILABLE ?
                <button disabled={!plays} className="column-selector-text" onClick={onClick}>
                    <div className={`checker ${isFalling ? 'checker-falling' : ''}`} style={checkerStyle}>
                        {playerNumber === 1 ? "🔵" : "🔴"}
                    </div>
                </button> :
                <button disabled={!plays} className="column-selector-text" onClick={() => alert("Column is full! Please choose another column")}>
                    {"✖"}
                </button>

            }
        </div>
    )
}

export default ColumnSelector;