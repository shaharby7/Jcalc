import React from 'react'
import { NavLink } from 'react-router-dom'

import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Typography from '@material-ui/core/Typography';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import { PagesConfig } from '../configs/pages.js';

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    title: {
        flexGrow: 1,
    },
}));

function JcalcMenuItem(pageDesctiption, pageLocation, handleClose) {
    return <MenuItem key={"menuItem for " + pageDesctiption}
        onClick={handleClose}>
        <NavLink to={"/" + pageLocation}>
            {pageDesctiption}
        </NavLink>
    </MenuItem>
}


export default function JcalcAppBar() {
    const classes = useStyles();
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);

    const handleMenu = event => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    const getMenuItems = () => {
        let menuItems = [JcalcMenuItem("Home", "", handleClose)];
        for (const [pageDesctiption, pageLocation] of Object.entries(PagesConfig)) {
            menuItems.push(
                JcalcMenuItem(pageDesctiption, pageLocation, handleClose)
            );
        }
        return menuItems;
    }

    return (
        <div className={classes.root}>
            <AppBar position="static">
                <Toolbar>
                    <div>
                        <IconButton edge="start"
                            className={classes.menuButton}
                            color="inherit"
                            aria-label="menu"
                            onClick={handleMenu}>
                            <MenuIcon />
                        </IconButton>
                        <Menu
                            id="menu-appbar"
                            anchorEl={anchorEl}
                            anchorOrigin={{
                                vertical: 'top',
                                horizontal: 'right',
                            }}
                            keepMounted
                            transformOrigin={{
                                vertical: 'top',
                                horizontal: 'right',
                            }}
                            open={open}
                            onClose={handleClose}
                        >
                            {getMenuItems()}
                        </Menu>
                    </div>
                    <Typography variant="h6" className={classes.title}>
                        Jcalc!
                    </Typography>
                </Toolbar>
            </AppBar>
        </div >
    )
}
