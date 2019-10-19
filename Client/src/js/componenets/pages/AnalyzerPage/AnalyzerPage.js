import React from 'react'
import AnalyzerPageForm from './AnalyzerPageForm'
import CommonResultsPane from '../../commons/CommonResultsPane/CommonResutlsPane'
import SuggestionsPane from '../../commons/SuggestionsPane/SuggestionsPane'
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

    hasProblems = () => {
        if (Object.keys(this.state.analyzedPattern).length > 0) {
            if (Object.keys(this.state.analyzedPattern.problems).length > 0) {
                return true;
            }
        }
        return false

    }

    render() {
        return <div>
            <h1>Analyze your pattern!</h1>
            <AnalyzerPageForm updatePattern={this.setPattern} />
            {this.hasProblems() || (Object.keys(this.state.analyzedPattern).length > 0) ?
                <SuggestionsPane siteswap={this.state.analyzedPattern.siteswap} /> :
                <div />
            }
            <CommonResultsPane
                titleText={`Results for analyzing siteswap ${this.state.analyzedPattern.siteswap}`}
                successMessage={"It's a great siteswap :)"}
                data={this.state.analyzedPattern} />

        </div>;
    }
}