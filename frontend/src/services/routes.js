import Config from "../config";

const Routes = {
    CART: {
        GET_USER_CART: Config.hostDevelopement + '/api/carts/get_user_cart/',
        ADD_TO_CART: Config.hostDevelopement + '/api/carts/add_to_cart/',
        REMOVE_FROM_CART: Config.hostDevelopement + '/api/carts/remove_from_cart/',
    },
    AUTH: {
        LOGIN: Config.hostDevelopement + '/api/auth/login/',
        REGISTER:  Config.hostDevelopement + '/api/auth/register/',
        LOGOUT: Config.hostDevelopement + '/api/auth/logout/',
        REFRESH: Config.hostDevelopement  +'api/auth/login/refresh/',
    }
}

export default Routes;