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
        <el-form-item prop="password">
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
          <el-button @click="submitForm('registerForm')">注册</el-button>
        </el-form-item>
        <el-form-item>
          <el-button @click="resetForm('registerForm')">重置</el-button>
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
      //正则表达式，匹配汉字、数字、字母、下划线且不能以下划线开头和结尾
      let patt = /^(?!_)(?!.*?_$)[a-zA-Z0-9_\u4e00-\u9fa5]+$/;
      if (value === "") {
        callback(new Error("用户名不能为空"));
      } else if (!patt.test(value)) {
        callback(
          new Error(
            "用户名只能包含汉字、数字、字母、下划线且不能以下划线开头和结尾"
          )
        );
      } else {
        //检查用户名是否重复
        axios
          .get("/flask/user/name", {
            params: {
              nickname: value
            }
          })
          .then(response => {
            if (response.data.status === 131) {
              callback(new Error("网络错误"));
            } else if (response.data.status === 132) {
              if (!response.data.exist) {
                callback();
              } else {
                callback(new Error("用户名已存在"));
              }
            }
          });
      }
    };
    //密码验证
    let validatePassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        if (this.registerForm.checkpassword !== "") {
          this.$refs.registerForm.validateField("checkpassword");
        }
        callback();
      }
    };
    //重复密码
    let validateCheckPassword = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.registerForm.password) {
        callback(new Error("两次输入密码不一致!"));
      } else {
        callback();
      }
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
          {
            min: 8,
            max: 18,
            message: "密码长度在 8 到 18 个字符",
            trigger: "blur"
          },
          { validator: validatePassword, trigger: "blur" }
        ],
        checkpassword: [
          {
            min: 8,
            max: 18,
            message: "密码长度在 8 到 18 个字符",
            trigger: "blur"
          },
          { validator: validateCheckPassword, trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          axios
            .post("/flask/user/register", {
              email: this.registerForm.email,
              password: this.registerForm.password,
              nickname: this.registerForm.nickname
            })
            .then(response => {
              if (
                response.data.status === 111 ||
                response.data.status === 114
              ) {
                this.$message.error("网络提交出错");
              } else if (response.data.status === 113) {
                this.$message({
                  message: "邮箱已被注册",
                  type: "warning"
                });
              } else if (response.data.status === 112) {
                this.$message({
                  message: "注册成功",
                  type: "success"
                });
                this.$router.push("/login");
              } else {
                this.$message.error("未知错误");
              }
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
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
  margin: 0 auto;
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
