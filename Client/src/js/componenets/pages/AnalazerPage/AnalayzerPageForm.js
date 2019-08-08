import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';



const useStyles = makeStyles(theme => ({
    container: {
        display: 'flex',
        flexWrap: 'wrap',
    },
    textField: {
        marginLeft: theme.spacing(1),
        marginRight: theme.spacing(1),
        width: 200,
    },
    button: {
        margin: theme.spacing(1),
    },
    input: {
        display: 'none',
    },
}));


export default function AnalayzerPageForm(props) {

    
    const classes = useStyles();

    const [siteswap, setSiteswap] = React.useState("");

    const onSubmit = () => {
        props.updatePattern(siteswap);
        setSiteswap("");
    }

    return <form className={classes.container} noValidate autoComplete="off">
        <TextField
            id="standard-password-input"
            label="Pattern"
            className={classes.textField}
            margin="normal"
            value={siteswap}
            onChange={(e) => setSiteswap(e.target.value)}
        />
        <Button variant="contained" className={classes.button} onClick={onSubmit}>
            Analyze!
            </Button>
    </form>
};