import React from "react";

function Homepage() {

    return(
        <div className="grid">
            <div className="nav">
                <p>Devices</p>
                <p>Games</p>
                <p>Developers</p>
            </div>
            <div className="home-content">
                <div className="home1">
                    <img src="/assets/nintendo-logo.png" alt="Hi"/>
                </div>
                <div className="home1">
                    <img src="/assets/sony-logo.png" alt="Hi"/>
                    <img src="/assets/microsoft-logo.png" alt="Hi"/>
                </div>
            </div>
        </div>
    )
}

export default Homepage