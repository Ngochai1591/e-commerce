import * as Actions from '../../actions/cart';


const initialState = {
    cart_id: null,
    items: [],

    getUserCartSuccess: false,
    getUserCartError: null,

    addToCartSuccess: false,
    addToCartError: null,

    removeFromCartSuccess: false,
    removeFromCartError: null,
}

const cartReducer = (state = initialState, action) =>{
    switch(action.type){
        //========REMOVE FROM CART
        case Actions.REMOVE_FROM_CART:{
            return{
                ...state,
                cart_id: null,
                items: [],
                removeFromCartSuccess: false,
                removeFromCartError: null
            }
        }

        case Actions.REMOVE_FROM_CART_SUCCESS:{
            return{
                ...state,
                cart_id: action.payload.cart.id,
                items: action.payload.cart.items,
                removeFromCartSuccess: true,
                removeFromCartError: null,
            }
        }

        case Actions.REMOVE_FROM_CART_ERROR:{
            return{
                ...state,
                 cart_id: null,
                 items: [],
                 removeFromCartError: action.payload,
                 removeFromCartSuccess: false,
            }
        }

        //========GET USER CART
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
        
        case Actions.GET_USER_CART_ERROR:{
            return{
                ...state,
                cart_id: null,
                items: [],
                getUserCartError: action.payload,
                getUserCartSuccess: false,
            }
        }

        //========ADD TO CART
        case Actions.ADD_TO_CART:{
            return{
                ...state,
                cart_id: null,
                items: [],
                addToCartSuccess: false,
                addToCartError: null,
            }
        }

        case Actions.ADD_TO_CART_SUCCESS:{
            return{
                ...state,
                cart_id: action.payload.cart_id,
                items: action.payload.items,
                addToCartSuccess: true,
                addToCartError: null,
            }
        }

        case Actions.ADD_TO_CART_ERROR:{
            return{
                ...state,
                cart_id: null,
                items: [],
                addToCartSuccess: false,
                addToCartError: action.payload
            }
        }

        //========Default
        default: {
            return state;
          }
      
    }
}

export default cartReducer;

