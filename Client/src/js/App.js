import React, { Component } from 'react'
import JcalcAppBar from './componenets/JcalcAppBar'
import AppSwitch from './componenets/JcalcAppSwitch'
import { HashRouter as Router} from 'react-router-dom'


class App extends Component {
    render() {
        return (
            <Router>
                <JcalcAppBar />
                <AppSwitch />
            </Router>
        )
    }
}

class Appd extends Component {
    render() {
        return (
            <Router>
                <Nav />
                <AppSwitch />
            </Router>
        )
    }
}



export default App