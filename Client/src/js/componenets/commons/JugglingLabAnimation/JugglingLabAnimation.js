import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        minHeight: 30,
        maxWidth: 752,
        background: theme.palette.secondary.main,
        margin: theme.spacing(4, 0, 2),
    },
    button: {
        textTransform: "none",
        flexGrow: 1
    }
}));


export default function JugglingLabAnimation(props) {
    const classes = useStyles();
    // React.useEffect(() => setAnswer(""), [props.siteswap]);

    const renderButton = () =>
        <Button onClick={() => window.open(`https://jugglinglab.org/anim?${props.siteswap}`)}
            className={classes.button}
            fullWidth>
            <Typography variant='body2'>
                {`View animation for ${props.siteswap} on JugglingLab!`}
            </Typography>
        </Button>

    return <Grid className={classes.root} container
        spacing={0}
        align="center"
        justify="center"
        direction="column" >
        {renderButton()}
    </ Grid>
}