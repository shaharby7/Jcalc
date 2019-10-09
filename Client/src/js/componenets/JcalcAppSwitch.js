import React from 'react';
import { Route, Switch } from 'react-router-dom';
import { PagesConfig } from '../configs/pages.js';
import * as pages from './pages/index';

function AppRoute(routeComponent) {
    const CompontetDestination = require(`./pages/${routeComponent}/${routeComponent}`).default;
    return (<Route path={`/${routeComponent}`}
        component={CompontetDestination}
        key={`Route to ${routeComponent}`} />);
}

function AppSwitch() {
    let Routes = Object.values(PagesConfig).map(AppRoute);
    return (<Switch>
        <Route exact path="/" component={pages.HomePage} />
        {Routes}
        <Route component={NotFound} />
    </Switch>);
}

const NotFound = () => <h1>404.. This page is not found!</h1>

export default AppSwitch