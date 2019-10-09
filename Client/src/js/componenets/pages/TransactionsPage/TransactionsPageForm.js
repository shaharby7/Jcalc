import React, { useReducer } from 'react';
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


export default function TransactionsPageForm(props) {


    const classes = useStyles();

    const [state, setState] = useReducer(
        (state, newState) => ({ ...state, ...newState }),
        {
            siteswap1: '',
            siteswap1: ''
        }
    );

    const handleChange = evt => {
        const { name, value } = evt.target;
        setState({ [name]: value });
    };

    const onSubmit = () => {
        props.updatePattern(state.siteswap1, state.siteswap2);
    }

    return <form className={classes.container} noValidate autoComplete="off">
        <TextField
            name="siteswap1"
            label="First siteswap"
            className={classes.textField}
            margin="normal"
            value={state.siteswap1}
            onChange={handleChange}
        />
        <TextField
            name="siteswap2"
            label="Seconed siteswap"
            className={classes.textField}
            margin="normal"
            value={state.siteswap2}
            onChange={handleChange}
        />
        <Button variant="contained" className={classes.button} onClick={onSubmit}>
            Find transaction!
        </Button>
    </form>
};