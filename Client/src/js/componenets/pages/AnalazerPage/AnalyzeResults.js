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

const getMessgeAvatar = (messageType) => {
    const imagePath = `/public/${messageType}.png`;
    return <Avatar
        alt="Remy Sharp"
        src={imagePath}
        // className={classes.avatar}
    />;
}


const genarateResultItem = (message) => {
    const messageType = message[0];
    const messageText = message[1]
    return <ListItem key={messageText}>
        <ListItemAvatar>
            {getMessgeAvatar(messageType)}
        </ListItemAvatar>
        <ListItemText
            primary={messageText}
        />
    </ListItem>
}

export default function AnalyzeResults(props) {
    const classes = useStyles();

    return (
        <div className={classes.root}>
            <Grid container spacing={2}>
                <Grid item xs={12} md={6}>
                    <Typography variant="h6" className={classes.title}>
                        Anatilze Results:
            </Typography>
                    <div className={classes.demo}>
                        <List>
                            {props.messages.map(
                                genarateResultItem
                            )}
                        </List>
                    </div>
                </Grid>
            </Grid>
        </div>
    );
}