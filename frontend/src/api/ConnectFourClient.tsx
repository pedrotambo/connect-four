import axios from "axios";

const baseBackendUrl = 'http://ec2-54-87-213-213.compute-1.amazonaws.com:8000';

const playerBoard = (playerId: string) => {
    return axios.get(`${baseBackendUrl}/games/${playerId}`)
                .then(response => response.data);
}

const dropChecker = (playerId: string, columnNumber: number) => {
    return axios.get(`${baseBackendUrl}/games/${playerId}/drops/${columnNumber.toString()}`)
                .then(response => response.data);
}

const resetGame = (gameId: string) => {
    return axios.get(`${baseBackendUrl}/reset/${gameId}`)
                .then(response => response.data);
}

const queries = {
    playerBoard,
    dropChecker,
    resetGame,
}

export default queries;

