import React from 'react';
import {
  HashRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import ConnectFourGame from '../game/ConnectFourGame'
import Home from '../home/Home'

function NavBar() {
  return <Router basename="/#">
    <div className="NavBar">
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/player1">Player 1</Link>
        </li>
        <li>
          <Link to="/player2">Player 2</Link>
        </li>
        <li>
          <Link to="/singleplayer">Singleplayer</Link>
        </li>
      </ul>
    </div>
    <Switch>
      <Route path="/player1">
        <ConnectFourGame playerNumber={1} playerId={"1"} gameId={"multiPlayerGame"} refetchIntervalMs={1000} singlePlayer={false} />
      </Route>
      <Route path="/player2">
        <ConnectFourGame playerNumber={2} playerId={"2"} gameId={"multiPlayerGame"} refetchIntervalMs={1000} singlePlayer={false}/>
      </Route>
      <Route path="/singleplayer">
        <ConnectFourGame playerNumber={1} playerId={"3"} gameId={"singlePlayerGame"} refetchIntervalMs={1000} singlePlayer={true}/>
      </Route>
      <Route path="/">
        <Home />
      </Route>
    </Switch>
  </Router>
}

export default NavBar;