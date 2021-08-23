import axios from "axios";

const player_board = (player_id: number) => {
    return axios.get(`http://localhost:8000/games/${player_id.toString()}`)
                .then(response => response.data);
}

const queries = {
    player_board,
}

export default queries;


