import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route, 
    Link
  } from "react-router-dom";
import ConnectFourGame from '../game/ConnectFourGame'
import Home from '../home/Home'

function NavBar() {
    return <Router>
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
        </ul>
    </div>
    <Switch>
        <Route path="/player1">
            <ConnectFourGame playerNumber={1} playerId={"1"}/>
        </Route>
        <Route path="/player2">
            <ConnectFourGame playerNumber={2} playerId={"2"} />
        </Route>
        <Route path="/">
            <Home />
        </Route>
    </Switch>
  </Router>
}

export default NavBar;