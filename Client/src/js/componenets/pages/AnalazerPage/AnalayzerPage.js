import React from 'react'
import AnalayzerPageForm from './AnalayzerPageForm.js'
import AnalyzeResults from './AnalyzeResults.js'
import { analyzeService } from './../../../backendHandlers/backendHandlers.js'

export default class AnalayzerPage extends (React.Component) {
    constructor(props) {
        super(props);
        this.state = {
            "analyzedPattern": {}
        }
    };

    setPattern = async (siteswap) => {
        const pattern = await analyzeService(siteswap);
        this.setState({ "analyzedPattern": pattern });
    };

    render() {
        return <div>
            <h1>Analyze your pattern!</h1>
            <AnalayzerPageForm updatePattern={this.setPattern} />
            {(Object.keys(this.state.analyzedPattern).length>0)?
                <AnalyzeResults pattern={this.state.analyzedPattern} />:null}
        </div>;
    }
}