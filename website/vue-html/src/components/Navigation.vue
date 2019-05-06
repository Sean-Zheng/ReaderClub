<template>
  <div id="navigation">
    <div class="ico-box">
      <img src="../assets/logo.png" width="45px" alt="logo">
      <router-link to="/">
        <strong>Reader Club</strong>
      </router-link>
    </div>
    <div class="center">
      <div class="search-box">
        <el-input placeholder="输入需要搜索的小说" v-model="search_key" @keyup.enter.native="search()">
          <el-button slot="suffix" type="text" icon="el-icon-search" circle @click="search()"></el-button>
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
      search_key: ""
    };
  },
  computed: {
    login() {
      return false;
    }
  },
  methods: {
    search() {
      if (this.search_key === "") {
        this.$message({
          message: "请输入所要搜索的内容",
          type: "warning"
        });
      } else {
        this.$router.push({
          name: "search",
          query: {
            keyword: this.search_key
          }
        });
        this.search_key = "";
      }
    }
  }
};
</script>

<style scoped>
#navigation {
  background-color: rgba(189, 195, 199, 0.4);
  height: 55px;
  display: flex;
  align-items: center;
}
#navigation div {
  display: inline-block;
}
.ico-box {
  box-sizing: border-box;
  width: 55%;
  padding-left: 300px;
  display: inline-flex !important;
  align-items: center;
}
.ico-box a {
  user-select: none;
  white-space: nowrap;
  display: inline-block;
  padding: 0 30px;
  text-decoration: none;
  color: #2c3e50;
}
.center {
  display: inline-flex !important;
  align-items: center;
}
.search-box {
  margin: 0 40px;
  width: 300px;
}
.search-box >>> input {
  background-color: #ecf0f1;
  border: 0px;
  color: #2c3e50;
}
.search-box >>> button {
  color: #2c3e50;
}
.user-box {
  display: inline-flex !important;
  align-items: center;
}
.user-box >>> a {
  white-space: nowrap;
  user-select: none;
  text-decoration: none;
  color: #2c3e50;
  padding: 0 30px;
}
.user-box img {
  border-radius: 50%;
}
</style>