import React from "react";

const getCell = (cellStatus: number) => {
    if (cellStatus > 1) {
        return 456;
    } else {
        return 123;
    }
}

function Cell({cellStatus}: {cellStatus: number}) {
    return (
        <div>
            {getCell(cellStatus)}
        </div>
    )
    
}


export default Cell;