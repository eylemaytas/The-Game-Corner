import React from "react";

function Game({game}) {
    
    return(
        <div className="game-card">
            <img src={game.image} alt="Hi" />
            <h2>{game.name}</h2>
        </div>
    )
}

export default Game