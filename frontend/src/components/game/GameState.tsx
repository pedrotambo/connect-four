type GameState = {
    board: number[][],
    plays: boolean,
    availableColumns: number[],
    isOver: boolean,
    wasWon: boolean,
    winner: string | undefined | null,
    wasTied: boolean
}

export default GameState;