export const REMOVE_FROM_CART = '@cart/REMOVE_FROM_CART';
export const UPDATE_CART_ITEM_QUANTITY = '@cart/UPDATE_CART_ITEM_QUANTITY';



//========ADD TO CART
export const ADD_TO_CART = '@cart/ADD_TO_CART';
export const ADD_TO_CART_SUCCESS = '@cart/ADD_TO_CART_SUCCESS';
export const ADD_TO_CART_ERROR = '@cart/ADD_TO_CART_ERROR';

export const addToCartSuccess = (data) =>{
    return 
}

export const addToCart = (token, product_id, quantity) =>{
    return{
        type: ADD_TO_CART ,
        token,
        product_id,
        quantity
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
        
    }
}




export const removeFromCart = (cart_id, product_id) =>{
    return{
        type: REMOVE_FROM_CART,
        cart_id, 
        product_id
    }
};

export const updateCartItemQuantity =(cart_id, product_id, quantity) =>{
    return{
        type: UPDATE_CART_ITEM_QUANTITY,
        cart_id,
        product_id,
        quantity
    }
};

