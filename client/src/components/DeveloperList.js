import React from "react";
import Developer from "./Developer";

function DeveloperList({developers}) {

    const developer = developers.map(developer => {
        return <Developer developer={developer} />
    })
    return(
        <div className="developer-grid">
            {developer}
        </div>
    )
}

export default DeveloperList