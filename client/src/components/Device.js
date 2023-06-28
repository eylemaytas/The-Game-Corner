import React from "react";

function Device({device}) {

    return(
        <div className="device-card">
            <img src={device.image} alt="Hi" />
            <h2>{device.name}</h2>
            <p>{device.type}</p>
        </div>
    )
}

export default Device