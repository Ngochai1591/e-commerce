import axios from 'axios';
import Routes from '../routes';

class cartService{
    getUserCart = (token) =>{
        return new Promise((resolve, reject)=>{
            axios.get(
                Routes.CART,
                {
                    headers:{
                        Accept: 'application/json',
                        Authorization: "Token " + token
                    }
                },
            ).then((res)=>{
                if(res.status === 200 && res.data){
                    resolve(res.data);
                }
            }).catch((err)=>{
                reject(err.response ? err.response.data : null);
            });
        })
    }

    addToCart = (token, product_id) =>{
        return new Promise((resolve, reject)=>{
            axios.post(
                Routes.CART.ADD_TO_CART,
                {
                    product_id: product_id,
                },
                {
                    headers:{
                        Accept: 'application/json',
                        Authorization: "Token " + token
                    }
                },
            ).then((res)=>{
                if(res.status === 200 & res.data){
                    resolve(res.data);
                }
            }).catch((err)=>{
                reject(err.response ? err.response.data: null)
            });
        })
    }

    removeFromCart = (token, product_id) =>{
        return new Promise((resolve, reject)=>{
            axios.post(
                Routes.CART.REMOVE_FROM_CART,
                {
                    product_id: product_id
                },
                {
                    headers:{
                        Accept: 'application/json',
                        Authorization: "Token " + token
                    }
                },
            ).then((res)=>{
                if(res.status === 200 && res.data){
                    resolve(res.data);
                }
            }).catch((err)=>{
                reject(err.response ? err.response.data: null)
            });
        });
    }
}

export default cartService