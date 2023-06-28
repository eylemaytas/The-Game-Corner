import React from "react";
import Game from "./Game";

function GameList({games}) {

    const game = games.map(game => {
        return <Game game={game} />
    })

    return(
        <div className="game-grid">
            {game}
        </div>
    )
}

export default GameList