<template>
  <div class="comment-add">
    <el-input
      type="textarea"
      :autosize="{ minRows: 4, maxRows: 10}"
      placeholder="请输入内容"
      v-model="comment_text"
    ></el-input>
    <div class="block">
      <el-rate v-model="score" :colors="['#99A9BF', '#F7BA2A', '#FF9900']"></el-rate>
    </div>
    <el-button class="btn" type="primary" @click="submitComment()">提交评论</el-button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "comment-add",
  data() {
    return {
      comment_text: "",
      score: 0
    };
  },
  methods: {
    submitComment() {
      if (!this.$store.getters.getLoginResult) {
        this.$message({
          message: "请登录...",
          type: "warning"
        });
        this.$router.push("/login");
      } else if (this.comment_text === "") {
        this.$message({
          message: "请输入评论！",
          type: "warning"
        });
      } else if (this.score === 0) {
        this.$message({
          message: "请选择评分",
          type: "warning"
        });
      } else {
        axios
          .post(
            `${process.env.VUE_APP_FLASK_URL}/comment/add`,
            {
              book_name: this.name,
              book_author: this.author,
              comment_text: this.comment_text,
              score: this.score
            },
            {
              headers: {
                Authorization: this.$store.getters.getToken
              }
            }
          )
          .then(res => {
            if (res.data.status === 412) {
              this.$message({
                message: "添加成功",
                type: "success"
              });
              this.$emit("commentAddSuccess");
            } else {
              this.$message({
                message: "网络错误",
                type: "warning"
              });
            }
          })
          .catch(() => {
            this.$message({
              message: "未登录...",
              type: "warning"
            });
            this.$router.push("/login");
          });
      }
    }
  },
  props: {
    name: {
      type: String,
      default: "",
      required: true
    },
    author: {
      type: String,
      defaul: "",
      required: true
    }
  }
};
</script>

<style scoped>
.comment-add {
  width: 1000px;
  margin: 50px auto;
  overflow: auto;
}
.block {
  margin: 20px;
  width: 500px;
  float: left;
}
.btn {
  margin: 20px;
  float: right;
}
</style>