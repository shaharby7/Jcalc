import React from 'react'
import AnalyzerPageForm from './AnalyzerPageForm'
import AnalyzeResults from './AnalyzerResults.js'
import { defaultBackendRequest } from '../../../backendHandlers/backendHandlers.js'

export default class AnalyzerPage extends (React.Component) {
    constructor(props) {
        super(props);
        this.state = {
            "analyzedPattern": {}
        }
    };

    setPattern = async (siteswap) => {
        const pattern = await defaultBackendRequest("analyzer", [siteswap]);
        this.setState({ "analyzedPattern": pattern });
    };

    render() {
        return <div>
            <h1>Analyze your pattern!</h1>
            <AnalyzerPageForm updatePattern={this.setPattern} />
            {(Object.keys(this.state.analyzedPattern).length > 0) ?
                <AnalyzeResults pattern={this.state.analyzedPattern} /> : null}
        </div>;
    }
}