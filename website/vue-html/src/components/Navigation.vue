<template>
  <div id="navigation">
    <div class="ico-box">
      <img src="../assets/logo.png" width="45px" alt="logo">
      <p>
        <strong>Reader Club</strong>
      </p>
    </div>
    <div class="center">
      <div class="search-box">
        <el-input placeholder="输入需要搜索的小说">
          <el-button slot="suffix" type="text" icon="el-icon-search" circle></el-button>
        </el-input>
      </div>
      <div v-if="!login" class="user-box">
        <router-link to="#">登录</router-link>
        <router-link to="#">注册</router-link>
      </div>
      <div v-if="login" class="user-box">
          <img src="../assets/user.jpg" width="45px" alt="user image">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "navigation",
  computed: {
      login() {
          return true 
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
.ico-box p{
  display: inline-block;
  padding: 0 30px;
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
}
.user-box{
  display: inline-flex !important;
  align-items: center;
}
.user-box >>> a {
  text-decoration: none;
  color: #409eff;
  padding: 0 30px;
}
.user-box img{
  border-radius: 50%;
}
</style>