import React from "react";
import Cell from './Cell'

function Board({width, height}: {width: number, height: number}) {
    return (
        <div>
            <p> Hello! The board size is {width} x {height} </p>
            <Cell cellStatus={1}></Cell>
        </div>
    );
}

export default Board;