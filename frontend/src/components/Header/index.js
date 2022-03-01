import React from 'react';
import {Link} from 'react-router-dom';
import {MdShoppingBasket, MdStar} from 'react-icons/md';
import {connect} from 'react-redux';

import logo from '../../assets/image/logo.jpeg';
import {Cart,Container} from './styles';

const Header = ({cartLength}) =>{
    return(
        <Container>
            <Link to='/'>
                <img src={logo} alt="Shopping logo"/>
            </Link>
            <Cart to="/cart">
                <div>
                    <strong>Shopping cart</strong>
                    <span>{cartLength}</span>
                </div>
                <MdShoppingBasket size={36}/>
            </Cart>
        </Container>
    )
}

export default connect(state =>({
    cartLength: state.cart.length
}))(Header);