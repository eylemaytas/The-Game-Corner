import React from "react";
import Device from "./Device";

function DeviceList({devices, deviceFocusSelector}) {

    const device = devices.map((device) => {
        return <Device device={device} deviceFocusSelector={deviceFocusSelector}/>
    })

    return(
        <div className="device-grid">
            {device}
        </div>
    )
}

export default DeviceList