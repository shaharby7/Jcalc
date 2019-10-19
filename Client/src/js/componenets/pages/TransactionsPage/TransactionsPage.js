import React from 'react'
import TransactionsPageForm from './TransactionsPageForm'
import { defaultBackendRequest } from '../../../backendHandlers/backendHandlers.js'
import CommonResultsPane from '../../commons/CommonResultsPane/CommonResutlsPane'

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

    render() {
        return <div>
            <h1>Find transacions between two siteswaps</h1>
            <TransactionsPageForm updatePattern={this.setPattern} />
            <CommonResultsPane titleText={"Transaction results"}
                successMessage={this.state.TransactionPattern.siteswap}
                data={this.state.TransactionPattern}
            />
        </div>;
    }
}