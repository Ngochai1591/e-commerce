import * as Actions from './actions';


const initialState = {
    cart_id: null,
    items: [],
    getUserCartSuccess: false,
    getUserCartError: null,
}

const reducer = (state = initialState, action) =>{
    switch(action.type){
        case Actions.GET_USER_CART:{
            return{
                ...state,
                cart_id: null,
                items: [],
                getUserCartError: null,
                getUserCartSuccess: false,
            }
        }

        case Actions.GET_USER_CART_SUCCESS:{
            return{
                ...state,
                cart_id: action.payload.cart.id,
                items: action.payload.cart.items,
                getUserCartError: null,
                getUserCartSuccess: true,

            }
        }
    }
}

