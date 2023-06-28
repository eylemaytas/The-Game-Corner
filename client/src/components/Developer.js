import React from "react";

function Developer({developer}) {

    return(
        <div className="developer-card">
            <img src={developer.logo} alt="hi" />
            <h2>{developer.name}</h2>
        </div>
    )
}

export default Developer