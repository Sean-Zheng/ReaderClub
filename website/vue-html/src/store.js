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
        home: {
            home_list: [],
            classification_list: []
        },
        typeLink: {
            玄幻魔法: 'https://www.biduo.cc/book_1_1/',
            武侠修真: 'https://www.biduo.cc/book_2_1/',
            都市言情: 'https://www.biduo.cc/book_3_1/',
            历史军事: 'https://www.biduo.cc/book_4_1/',
            网游动漫: 'https://www.biduo.cc/book_6_1/',
            科幻小说: 'https://www.biduo.cc/book_7_1/',
            恐怖灵异: 'https://www.biduo.cc/book_8_1/',
            其他小说: 'https://www.biduo.cc/book_10_1/'
        },
        theme: 'default'
    },
    getters: {
        getToken: state => {
            return `${state.authorization.type} ${state.authorization.token}`;
        },
        getLoginResult: state => {
            if (state.authorization.status === 122) {
                return true;
            }
            return false;
        },
        getHomeList: state => {
            return state.home.home_list;
        },
        getClassificationList: state => {
            return state.home.classification_list;
        },
        getTheme: state => {
            return state.theme;
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
        removeToken: state => {
            state.authorization.status = undefined;
            state.authorization.type = '';
            state.authorization.username = '';
            state.authorization.token = ''
        },
        setHomerecommend: (state, data) => {
            state.home.home_list = data.home_list;
            state.home.classification_list = data.classification_list;
        },
        setTheme: (state, theme) => {
            state.theme = theme;
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
        homeAction: async context => {
            const response = await axios.post('/scrapyrt', {
                spider_name: 'Home',
                request: {
                    url: 'https://www.biduo.cc/'
                }
            });
            context.commit('setHomerecommend', response.data.items[0]);
            return response.data.status;
        }
    }
})