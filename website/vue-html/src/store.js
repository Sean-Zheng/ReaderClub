import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        authorization: {
            status: undefined,
            type: '',
            token: '',
            username: ''
        }
    },
    getters: {
        getToken: state => {
            return `${state.authorization.type} ${state.authorization.token}`;
        },
        getLoginResult:state=>{
            if(state.authorization.status===122){
                return true;
            }
            return false;
        }
    },
    mutations: {
        setToken: (state, data) => {
            if (data.status === 122) {
                state.authorization.username = data.username;
                state.authorization.type = data.type;
                state.authorization.token = data.token;
            }
            state.authorization.status = data.status;
        },
        removeToken:state=>{
            state.authorization.status=undefined;
            state.authorization.type='';
            state.authorization.username='';
            state.authorization.token=''
        }
    },
    actions: {
        loginAction: async (context, payload) => {
            const response = await axios.post('/flask/user/login', {
                account: payload.account,
                password: payload.password
            });
            context.commit("setToken", response.data);
        }
    }
})