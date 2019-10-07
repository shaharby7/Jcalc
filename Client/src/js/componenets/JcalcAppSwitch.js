import React, { Component } from 'react'
import { Route, Switch } from 'react-router-dom'
import AnalayzerPage from './pages/AnalazerPage/AnalayzerPage'
import HomePage from './pages/HomePage/HomePage'

const AppSwitch = () => (
    <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/AnalyzerPage" component={AnalayzerPage} />
        <Route component={NotFound} />
    </Switch>
)

const NotFound = () => <h1>404.. This page is not found!</h1>

export default AppSwitch