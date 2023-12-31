import React from 'react';
import ReactDOM from 'react-dom/client';
import { ThemeProvider } from "@mui/material/styles";
import { CssBaseline } from "@mui/material";
import theme from "./Komponente/Theme.js";
import App from "./App.js"
import { BrowserRouter as Router} from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <ThemeProvider theme={theme}>
    <Router>
        <CssBaseline />
           <App/>
    </Router>
    </ThemeProvider>
);


