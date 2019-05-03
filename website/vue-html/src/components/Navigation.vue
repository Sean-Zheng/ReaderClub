<template>
  <div id="navigation">
    <div class="ico-box">
      <img src="../assets/logo.png" width="45px" alt="logo">
      <router-link to="/"><strong>Reader Club</strong></router-link>
    </div>
    <div class="center">
      <div class="search-box">
        <el-input placeholder="输入需要搜索的小说" v-model="search_key">
          <el-button slot="suffix" type="text" icon="el-icon-search" circle></el-button>
        </el-input>
      </div>
      <div v-if="!login" class="user-box">
        <router-link to="/login">登录</router-link>
        <router-link to="/register">注册</router-link>
      </div>
      <div v-if="login" class="user-box">
          <img src="../assets/user.jpg" width="40px" alt="user image">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "navigation",
  data() {
    return {
      search_key: ''
    }
  },
  computed: {
      login() {
          return false; 
      }
  },
};
</script>

<style scoped>
#navigation {
  background-color: rgb(136, 139, 140);
  height: 55px;
  display: flex;
  align-items: center;
}
#navigation div{
    display: inline-block;
}
.ico-box{
    box-sizing: border-box;
    width: 55%;
    padding-left: 300px;
    display: inline-flex !important;
    align-items: center;
}
.ico-box a{
  display: inline-block;
  padding: 0 30px;
  text-decoration: none;
  color: rgb(217,217,217);
}
.center{
  display: inline-flex !important;
  align-items: center;
}
.search-box {
  margin: 0 40px;
  width: 300px;
}
.search-box >>> input {
  background-color: rgba(54, 65, 71, 0.5);
  border: 0px;
  color: white;
}
.search-box >>> button{
  color: rgb(217,217,217);
}
.user-box{
  display: inline-flex !important;
  align-items: center;
}
.user-box >>> a {
  text-decoration: none;
  color: rgb(217,217,217);
  padding: 0 30px;
}
.user-box img{
  border-radius: 50%;
}
</style>