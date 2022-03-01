import React, { Component } from 'react';
import {Route, Switch, Redirect} from 'react-router-dom';

import Home from './pages/Home';
import Auth from './pages/Auth';
import Cart from './pages/Cart';

const PrivateRoute = ({component: Component, ...rest})=>{
    return(
        <Route {...rest} 
            render={props =>{
                
            }}
    )
}