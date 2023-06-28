import React from "react";
import Device from "./Device";

function DeviceList({devices}) {

    const device = devices.map((device) => {
        return <Device device={device} />
    })

    return(
        <div className="device-grid">
            {device}
        </div>
    )
}

export default DeviceList