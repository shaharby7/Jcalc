import React from 'react'
import TransactionsPageForm from './TransactionsPageForm'
import { defaultBackendRequest } from '../../../backendHandlers/backendHandlers.js'

export default class TransactionsPage extends (React.Component) {
    constructor(props) {
        super(props);
        this.state = {
            "TransactionPattern": {}
        }
    };

    setPattern = async (siteswap1, siteswap2) => {
        const pattern = await defaultBackendRequest("transactions", [siteswap1, siteswap2]);
        this.setState({ "TransactionPattern": pattern });
    };

    render() {
        return <div>
            <h1>Find transacions between two siteswaps</h1>
            <TransactionsPageForm updatePattern={this.setPattern} />
            <p>{this.state.TransactionPattern.siteswap}</p>
        </div>;
    }
}