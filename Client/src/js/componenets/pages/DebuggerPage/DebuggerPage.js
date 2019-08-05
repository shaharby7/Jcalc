import React from 'react'
import DebuggerPageForm from './DebuggerPageForm.js'

export default class DebuggerPage extends (React.Component) {
    render() {
        const form = DebuggerPageForm();
        return <div>
            {form}
        </div>
    }
}