import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import ListItemText from '@material-ui/core/ListItemText';
import Avatar from '@material-ui/core/Avatar';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import JugglingLabAnimation from '../JugglingLabAnimation/JugglingLabAnimation'

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        maxWidth: 752
    },
    title: {
        margin: theme.spacing(4, 0, 2),
    },
    avatar: {
        margin: 10,
    },
}));

const createMessagesList = (successMessage, data) => {
    if (data.success) {
        if (data.problems.length === 0) {
            return [{
                "message": successMessage,
                "faviconPath": "/public/success.png"
            }];
        } else {
            return data.problems.map((problem) => {
                return {
                    "message": problem.message,
                    "problematicBeat": problem.problematic_beat,
                    "faviconPath": `/public/generic_problem.png`
                };
            });
        }
    } else {
        return [{
            "message": data.message,
            "problematicBeat": data.problematic_beat,
            "faviconPath": "/public/parsing_error.png"
        }];
    }
}

const renderMessagesList = (messagesList) => {
    const classes = useStyles();
    return messagesList.map((messageObject) =>
        <ListItem key={`ListItem for ${messageObject.message}`}>
            <ListItemAvatar className={classes.avatar}>
                <Avatar
                    alt="Remy Sharp"
                    src={messageObject.faviconPath}
                />
            </ListItemAvatar>
            <ListItemText
                primary={messageObject.message}
                secondary={messageObject.problematicBeat ?
                    `Problematic beat: ${messageObject.problematicBeat}` :
                    null}
            />
        </ListItem>
    );
}

export default function CommonResultsPane(props) {
    if (Object.keys(props.data).length === 0) {
        return <div />;
    }
    const classes = useStyles();
    const messagesList = createMessagesList(props.successMessage, props.data);

    const renderJugglingLabAnimation = () => {
        if (props.data.success) {
            if (props.data.problems.length === 0) {
                return <JugglingLabAnimation siteswap={props.data.siteswap} />;
            }
        };
        return <div/>
    }
    return (
        <div className={classes.root}>
            {renderJugglingLabAnimation()}
            <Grid container spacing={2}>
                <Grid item xs={12} md={6}>
                    <Typography variant="h6" className={classes.title}>
                        {props.titleText}
                    </Typography>
                    <div>
                        <List>
                            {renderMessagesList(messagesList)}
                        </List>
                    </div>
                </Grid>
            </Grid>
        </div>
    )
}
