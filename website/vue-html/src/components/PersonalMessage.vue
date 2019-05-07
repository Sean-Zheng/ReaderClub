<template>
  <div class="personal-message">
    <div class="wrap">
      <div class="msg">
        <img class="avatar-box" src="../assets/user.jpg" alt width="100" height="100">
        <div class="info">
          <h2>{{username}}</h2>
          <el-input v-model="signature"></el-input>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "personal-message",
  data() {
    return {
      username: "",
      signature: ""
    };
  },
  created() {
    if (!this.$store.getters.getLoginResult) {
      this.$router.push("/login");
    } else {
      this.username = this.$store.state.authorization.username;
      this.signature = this.$store.state.authorization.signature;
    }
  }
};
</script>

<style scoped>
.personal-message {
  background-image: url("../assets/space.jpeg");
  background-size: contain;
  background-repeat: no-repeat;
  margin: 0 auto;
  width: 1080px;
  height: 420px;
}
.wrap {
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.3);
}
.avatar-box {
  border-radius: 50%;
  float: left;
  margin: 20px;
}
.msg {
  overflow: auto;
  padding-top: 280px;
}
.info {
  width: 50%;
  float: left;
  margin: 10px;
}
.info > h2 {
  padding-left: 15px;
  color: #ffffff;
}
.el-input >>> input {
  background-color: rgba(255, 255, 255, 0);
  border: 0px;
  color: #ffffff;
}
.el-input >>> input:hover {
  background-color: rgba(255, 255, 255, 0.4);
  border: 0px;
  color: #ffffff;
}
</style>