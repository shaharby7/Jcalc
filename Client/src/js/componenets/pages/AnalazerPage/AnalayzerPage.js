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

    messageList = () => {
        if (Object.keys(this.state.analyzedPattern).length == 0) {
            return []
        }
        else {
            if (this.state.analyzedPattern.problems.length>0) {
                return this.state.analyzedPattern.problems.map(
                    (problem) => ["logical_failure", problem.message]
                );
            }
            else {
                return [["success", "Awesome siteswap :)"]];
            }
        }
    }

    render() {
        const messages = this.messageList();
        return <div>
            <h1>Analyze your pattern!</h1>
            <AnalayzerPageForm updatePattern={this.setPattern} />
            {(Object.keys(messages).length>0) ?
                <AnalyzeResults messages={messages} /> : null}
        </div>;
    }
}