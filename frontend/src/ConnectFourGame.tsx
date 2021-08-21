import React from 'react';
import './App.css';
import Board from './components/gameboard/Board'

function ConnectFourGame() {
  return (
    <div className="ConnectFourGame">
      <header className="ConnectFourGame-header">
        <Board width={7} height={6}></Board>
      </header>
    </div>
  );
}

export default ConnectFourGame;