import axios from "axios";

const playerBoard = (playerId: string) => {
    return axios.get(`http://localhost:8000/games/${playerId}`)
                .then(response => response.data);
}

const dropChecker = (playerId: string, columnNumber: number) => {
    return axios.get(`http://localhost:8000/games/${playerId}/drops/${columnNumber.toString()}`)
                .then(response => response.data);
}

const queries = {
    playerBoard,
    dropChecker,
}

export default queries;

