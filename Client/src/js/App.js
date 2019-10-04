import React, { Component } from 'react'
import { HashRouter as Router, Route, Link, Switch } from 'react-router-dom'
import AnalayzerPage from './componenets/pages/AnalazerPage/AnalayzerPage'
import HomePage from './componenets/pages/HomePage/HomePage'



class App extends Component {
    render() {
        return (
            <Router>
                <Nav />
                <AppSwitch />
            </Router>
        )
    }
}

const Nav = () => (
    <ul>
        <li>
            <Link to="/">HomePage</Link>
        </li>
        <li>
            <Link to="/analyzer">Analayzer</Link>
        </li>
    </ul>
)

const AppSwitch = () => (
    <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/analyzer" component={AnalayzerPage} />
        <Route component={NotFound} />
    </Switch>
)

const NotFound = () => <h1>404.. This page is not found!</h1>

export default App