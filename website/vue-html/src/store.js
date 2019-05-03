import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        //认证信息
        authorization: {
            status: undefined,
            type: '',
            token: '',
            username: ''
        },
        //首页推荐信息
        home:{
            home_list:[],
            classification_list:[]
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
        },
        getHomeList:state=>{
            return state.home.home_list;
        },
        getClassificationList:state=>{
            return state.home.classification_list;
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
        },
        setHomerecommend:(state,data)=>{
            state.home.home_list=data.home_list;
            state.home.classification_list=data.classification_list;
        }
    },
    actions: {
        loginAction: async (context, payload) => {
            const response = await axios.post('/flask/user/login', {
                account: payload.account,
                password: payload.password
            });
            context.commit("setToken", response.data);
        },
        homeAction:async context=>{
            const response= await axios.post('/scrapy/crawl.json',{
                spider_name:'Home',
                request:{
                    url:'https://www.biduo.cc/'
                }
            });
            // console.log(response.data.items);
            context.commit('setHomerecommend',response.data.items[0]);
            return response.data.status;
        }
    }
})