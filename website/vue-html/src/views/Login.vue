<template>
  <div
    id="login"
    v-loading.fullscreen.lock="loading"
    element-loading-text="登陆中..."
    element-loading-background="#343f45"
  >
    <div class="input-box">
      <el-form v-bind:model="loginForm" v-bind:rules="rules" ref="loginForm">
        <el-form-item prop="account">
          <el-input
            type="text"
            prefix-icon="el-icon-user"
            placeholder="用户名/邮箱"
            v-model="loginForm.account"
          ></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            type="password"
            prefix-icon="el-icon-lock"
            v-model="loginForm.password"
            autocomplete="off"
            placeholder="密码"
            @keyup.enter.native="login()"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button @click="login()">登录</el-button>
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
      loading: false,
      loginForm: {
        account: "",
        password: ""
      },
      rules: {
        account: [{ required: true, message: "请输入用户名", trigger: "blur" }],
        password: [
          { required: true, message: "请输入密码", trigger: "blur" },
          {
            min: 8,
            max: 18,
            message: "密码长度在 8 到 18 个字符",
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    login() {
      this.loading = true;
      this.$store
        .dispatch("loginAction", {
          account: this.loginForm.account,
          password: this.loginForm.password
        })
        .then(() => {
          if (this.$store.getters.getLoginResult) {
            this.loading = false;
            this.$message({
              message: "登陆成功",
              type: "success"
            });
            this.$router.push("/");
          } else {
            this.loading = false;
            this.$message({
              message: "登陆失败",
              type: "warning"
            });
          }
        });
    }
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
  margin: 0 auto;
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
