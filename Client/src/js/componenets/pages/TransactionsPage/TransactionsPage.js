import React from 'react';
import TransactionsPageForm from './TransactionsPageForm';
import { defaultBackendRequest } from '../../../backendHandlers/backendHandlers.js';
import CommonResultsPane from '../../commons/CommonResultsPane/CommonResutlsPane';
import SuggestionsPane from '../../commons/SuggestionsPane/SuggestionsPane';

const ProblematicSiteswapMessage = "Cannot create transaction for invalid pattern";

export default class TransactionsPage extends (React.Component) {
    constructor(props) {
        super(props);
        this.state = {
            "TransactionPattern": {},
            "BackendErrors": {}
        }
    };

    setPattern = async (siteswap1, siteswap2) => {
        const pattern = await defaultBackendRequest("transactions",
            [siteswap1, siteswap2]).catch((err) => {
                this.setState({ "BackendErrors": err })
            });
        this.setState({ "TransactionPattern": pattern });
    };

    hasPRoblematicSiteswap = () => {
        if (Object.keys(this.state.TransactionPattern).length > 0) {
            if (!this.state.TransactionPattern.success) {
                if (this.state.TransactionPattern.message == ProblematicSiteswapMessage) {
                    return true;
                }
            }
        }
        return false
    }

    render() {
        return <div>
            <h1>Find transacions between two siteswaps</h1>
            <TransactionsPageForm updatePattern={this.setPattern} />
            {this.hasPRoblematicSiteswap() ?
                <SuggestionsPane siteswap={this.state.TransactionPattern.siteswap} /> :
                <div />}
            <CommonResultsPane titleText={"Transaction results"}
                successMessage={this.state.TransactionPattern.siteswap}
                data={this.state.TransactionPattern}
            />
        </div>;
    }
}