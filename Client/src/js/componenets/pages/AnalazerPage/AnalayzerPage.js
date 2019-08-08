import React from 'react'
import AnalayzerPageForm from './AnalayzerPageForm.js'
import { analyzeService } from './../../../backendHandlers/backendHandlers.js'

export default class AnalayzerPage extends (React.Component) {
    constructor(props) {
        super(props);
        this.state = {
            "analyzedPattern": {}
        }
    };

    setPattern = (siteswap) => {
        const pattern = analyzeService(siteswap);
        this.setState({ "analyzedPattern": pattern });
        debugger;
    };

    render() {
        return <div>
            <h1>Analyze your pattern!</h1>
            <AnalayzerPageForm updatePattern={this.setPattern} />
        </div>;
    }
}