import '../App.css';
import {useState, useEffect} from 'react'
import { Route, Switch } from "react-router-dom"

import Login from './Login';
import Header from './Header';
import Footer from './Footer';
import Homepage from './Homepage';
import DeviceList from './DeviceList';
import GameList from './GameList';

function App() {

  const [devices, setDevices] = useState([])
  const [games, setGames] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:7000/devices')
    .then(res => res.json())
    .then(deviceData => setDevices(deviceData))
  }, [])

  useEffect(() => {
    fetch('http://127.0.0.1:7000/games')
    .then(res => res.json())
    .then(gameData => setGames(gameData))
  }, [])

  return (
    <div className="app">
      <Header />
      <Switch>
        <Route exact path="/">
          <Login />
        </Route>
        <Route exact path="/home">
          <Homepage />
        </Route>
        <Route exact path="/devices">
          <DeviceList devices={devices}/>
        </Route>
        <Route exact path="/games">
          <GameList games={games} />
        </Route>
      </Switch>
      <Footer />
    </div>
  );
}

export default App;