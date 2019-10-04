import React, { Component } from 'react'
import { BrowserRouter as Router, Route} from 'react-router-dom'
import AnalayzerPage from './pages/AnalazerPage/AnalayzerPage.js'
import HomePage from './pages/HomePage/HomePage.js'

export default class AppRouter extends Component {
    render() {
        return (
            <Router>
                <Route path='/' component={HomePage} />
                <Route path='/analyzer' component={AnalayzerPage} />
            </Router>
        )
    }
}
