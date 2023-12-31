import React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import WavingHandIcon from '@mui/icons-material/WavingHand';
import { useNavigate } from "react-router-dom";
import Logout from './Logout';

function LogovaniNavbar() {
  const navigate = useNavigate();
  const username = localStorage.getItem("username");
    return (
      <Box sx={{ flexGrow: 1 }}>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="paragraph" component="div" sx={{ flexGrow: 1 }}>
            <WavingHandIcon />
                 Hello {username}
            </Typography>
            <Button color="inherit" onClick = {() => navigate('/')}>Home</Button>
            <Button color = "inherit" onClick = {() => navigate('/logovani')}>Study</Button>
            <Logout/>
          </Toolbar>
        </AppBar>
      </Box>
    );
  }

  export default LogovaniNavbar;