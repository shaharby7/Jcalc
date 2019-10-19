import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { defaultBackendRequest } from '../../../backendHandlers/backendHandlers.js'


const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        minHeight: 30,
        maxWidth: 752,
        background: theme.palette.secondary.main,
        margin: theme.spacing(4, 0, 2),
    },
    typography: {
        textAlign: 'center',
        justify: 'center'
    },
    button: {
        textTransform: "none",
        flexGrow: 1
    }
}));


export default function SuggestionsPane(props) {
    const classes = useStyles();
    let [answer, setAnswer] = useState("");

    const activatePane = () => async () => {
        const response = await defaultBackendRequest("suggestions", [props.siteswap]);
        setAnswer(response.siteswap);
    }

    React.useEffect(() => setAnswer(""),[props.siteswap]);

    const renderButton = () =>
        <Button onClick={activatePane()}
            className={classes.button}
            fullWidth>
            <Typography variant='body2'>
                Suggest closest valid pattern to siteswap {props.siteswap}
            </Typography>
        </Button>

    const renderAnswer = () =>
        <Typography className={classes.typography} variant='body2'>
            {answer}
        </Typography>

    return <Grid className={classes.root} container
        spacing={0}
        align="center"
        justify="center"
        direction="column" >
        {answer ? renderAnswer() : renderButton()}
    </ Grid>
}