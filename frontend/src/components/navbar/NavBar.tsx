import React from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route, 
    Link
  } from "react-router-dom";
import ConnectFourGame from '../../ConnectFourGame'
import Home from '../../Home'

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
            <ConnectFourGame player_number={1} />
        </Route>
        <Route path="/player2">
            <ConnectFourGame player_number={2} />
        </Route>
        <Route path="/">
            <Home />
        </Route>
    </Switch>
  </Router>
}

export default NavBar;