<template>
  <div id="register">
    <div class="input-box">
      <el-form status-icon v-bind:model="registerForm" v-bind:rules="rules" ref="registerForm">
        <el-form-item prop="nickname">
          <el-input type="text" prefix-icon="el-icon-user" v-model="registerForm.nickname"></el-input>
        </el-form-item>
        <el-form-item prop="email">
          <el-input type="text" prefix-icon="el-icon-message" v-model="registerForm.email"></el-input>
        </el-form-item>
        <el-form-item prop="pass">
          <el-input
            type="password"
            prefix-icon="el-icon-lock"
            v-model="registerForm.password"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item prop="checkpassword">
          <el-input
            type="password"
            prefix-icon="el-icon-lock"
            v-model="registerForm.checkpassword"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-button>注册</el-button>
        </el-form-item>
        <el-form-item>
          <el-button>重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    //用户名验证
    let validateNickname = (rule, value, callback) => {
      console.log(rule);
      console.log(value);
    };
    //密码验证
    let validatePassword=(rule,value,callback)=>{

    };
    //重复密码
    let validateCheckPassword=(rule,value,callback)=>{

    };
    return {
      registerForm: {
        email: "",
        password: "",
        checkpassword: "",
        nickname: ""
      },
      rules: {
        nickname: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { validator: validateNickname, trigger: "blur" }
        ],
        email: [
          { required: true, message: "请输入邮箱地址", trigger: "blur" },
          {
            type: "email",
            message: "请输入正确的邮箱地址",
            trigger: ["blur", "change"]
          }
        ],
        password: [
            { validator: validatePassword, trigger: "blur" },
            { min: 8, max: 18, message: '密码长度在 8 到 18 个字符', trigger: 'blur' }
            ],
        checkpassword: [
            { validator: validateNickname, trigger: "blur" },
            { min: 8, max: 18, message: '密码长度在 8 到 18 个字符', trigger: 'blur' }
        ]
      }
    };
  }
};
</script>

<style scoped>
#register {
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
