<template>
  <div id="login">
    <div class="input-box">
      <el-form v-bind:model="loginForm" v-bind:relues="rules" ref="loginForm">
        <el-form-item prop="email">
          <el-input type="text" prefix-icon="el-icon-user" placeholder="用户名/邮箱" v-model="loginForm.email"></el-input>
        </el-form-item>
        <el-form-item prop="pass">
          <el-input
            type="password"
            prefix-icon="el-icon-lock"
            v-model="loginForm.password"
            autocomplete="off"
            placeholder="密码"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button>登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      loginForm: {
        email: "",
        password: ""
      },
      rules: {}
    };
  }
};
</script>

<style scoped>
#login {
  background-image: url("../assets/pages.jpg");
  background-size: contain;
  background-repeat: no-repeat;
  width: 460px;
  height: 400px;
  padding: 100px 0;
  display: flex;
  align-items: center;
}
.input-box {
  width: 250px;
  margin: 10px auto;
}
.input-box >>> button {
  background-color: rgb(136, 139, 140);
  color: rgb(217, 217, 217);
  width: 250px;
}
</style>
