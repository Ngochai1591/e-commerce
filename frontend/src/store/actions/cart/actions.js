import cartService from "../../../services/cartService";

// export const UPDATE_CART_ITEM_QUANTITY = '@cart/UPDATE_CART_ITEM_QUANTITY';


//========REMOVE FROM CART
export const REMOVE_FROM_CART = '@cart/REMOVE_FROM_CART';
export const REMOVE_FROM_CART_SUCCESS = '@cart/REMOVE_FROM_CART_SUCCESS';
export const REMOVE_FROM_CART_ERROR = '@cart/REMOVE_FROM_CART_ERROR';

export const removeFromCartSuccess = (data) =>{
    return(dispatch)=>{
        dispatch({
            type: REMOVE_FROM_CART_ERROR,
            payload: data
        });
    }
}

export const removeFromCartError = (err) =>{
    return(dispatch) =>{
        dispatch({
            type: REMOVE_FROM_CART_ERROR,
            payload: err
        });
    }
}

export const removeFromCart = (token, product_id) =>{
    return(dispatch)=>{
        dispatch({
            type: REMOVE_FROM_CART
        });

        cartService.removeFromCart(token, product_id).then((data)=>{
            if(data){
                dispatch(removeFromCartSuccess(data));
            }
        }).catch((err)=>{
            dispatch(removeFromCartError(err));
        });

    }
}

//========ADD TO CART
export const ADD_TO_CART = '@cart/ADD_TO_CART';
export const ADD_TO_CART_SUCCESS = '@cart/ADD_TO_CART_SUCCESS';
export const ADD_TO_CART_ERROR = '@cart/ADD_TO_CART_ERROR';

export const addToCartSuccess = (data) =>{
    return (dispatch) =>{
        dispatch({
            type: ADD_TO_CART_SUCCESS,
            payload: data
        });
    }
}

export const addToCartError = (err) =>{
    return(dispatch) =>{
        dispatch({
            type: ADD_TO_CART_ERROR,
            payload: err
        });
    }
}

export const addToCart = (token, product_id) =>{
    return(dispatch)=>{
        dispatch({
            type: ADD_TO_CART
        });
        cartService.addToCart(token, product_id).then((data)=>{
            if(data){
                dispatch(addToCartSuccess(data));
            }
        }).catch((err)=>{
            dispatch(addToCartError(err));
        })
    }
};

//========GET USER CART
export const GET_USER_CART = '@cart/GET_USER_CART';
export const GET_USER_CART_SUCCESS = '@cart/GET_USER_CART_SUCCESS';
export const GET_USER_CART_ERROR = '@cart/GET_USER_CART_ERROR';

export const getUserCartError = (error) =>{
    return(dispatch) =>{
        dispatch({
            type: GET_USER_CART_ERROR,
            payload: error
        })
    }
}

export const getUserCartSuccess = (data) =>{
    return(dispatch) =>{
        dispatch({
            type: GET_USER_CART_SUCCESS,
            payload: data
        });
    }
}

export const getUserCart = (token) =>{
    return (dispatch) =>{
        dispatch({
            type: GET_USER_CART
        });

        cartService.getUserCart(token).then((data)=>{
            dispatch(getUserCartSuccess(data));
        }).catch((err)=>{
            dispatch(getUserCartError(err));
        })

        
    }
}




