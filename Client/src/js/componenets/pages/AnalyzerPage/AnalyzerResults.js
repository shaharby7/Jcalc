import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import ListItemText from '@material-ui/core/ListItemText';
import Avatar from '@material-ui/core/Avatar';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        maxWidth: 752,
    },
    demo: {
        backgroundColor: theme.palette.background.paper,
    },
    title: {
        margin: theme.spacing(4, 0, 2),
    },
    avatar: {
        margin: 10,
    },
}));

const getMessgeAvatar = (problemKind) => {
    let imagePath = `/public/generic_problem.png`;
    if (problemKind == 'parsing_error') {
        imagePath = `/public/parsing_error.png`
    }
    return <Avatar
        alt="Remy Sharp"
        src={imagePath}
    />;
}


const genarateResultItem = (problem) => {
    return <ListItem key={problem.message}>
        <ListItemAvatar>
            {getMessgeAvatar(problem.kind)}
        </ListItemAvatar>
        <ListItemText
            primary={`Beat number: ${problem.problematic_beat}`}
            secondary={problem.message}
        />
    </ListItem>
}

export default function AnalyzeResults(props) {
    const classes = useStyles();

    const renderProblems = () => {
        return (
            <div className={classes.root}>
                <Grid container spacing={2}>
                    <Grid item xs={12} md={6}>
                        <Typography variant="h6" className={classes.title}>
                            {`Anatilze Results for siteswap: ${props.pattern.siteswap}`}
                        </Typography>
                        <div className={classes.demo}>
                            <List>
                                {props.pattern.problems.map(
                                    genarateResultItem
                                )}
                            </List>
                        </div>
                    </Grid>
                </Grid>
            </div>
        );
    }

    const renderSuccess = () => {
        return <div>
            <Typography variant="h6" className={classes.title}>
                {`The siteswap ${props.pattern.siteswap} is great!`}
            </Typography>
            <Avatar
                alt="Remy Sharp"
                src="/public/success.png"
            />
        </div>
    }

    return props.pattern.problems.length > 0 ? renderProblems() : renderSuccess();
}