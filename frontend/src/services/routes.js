import Config from "../config";

const Routes = {
    CART: {
        GET_USER_CART: Config.hostDevelopement + '/api/carts/get_user_cart/',
        ADD_TO_CART: '/api/carts/add_to_cart/',
        REMOVE_FROM_CART: '/api/carts/remove_from_cart/',
    },
    AUTH: {
        LOGIN: '/api/auth/login/',
        REGISTER: '/api/auth/register/',
        LOGOUT: '/api/auth/logout/',
        REFRESH: 'api/auth/login/refresh/',
    }
}

export default Routes;