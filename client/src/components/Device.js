import React from "react";

function Device({device, deviceFocusSelector}) {

    return(
        <div className="device-card">
            <img onClick={deviceFocusSelector} src={device.image} alt={device.id} />
            <h2>{device.name}</h2>
            <p>{device.type}</p>
        </div>
    )
}

export default Device