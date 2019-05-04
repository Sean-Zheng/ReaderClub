<template>
  <div id="chapter">
    <p>{{this.$route.query.url}}</p>
    <p v-html="content"></p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "chapter",
  data() {
      return {
          content: ''
      }
  },
  created() {
    axios
      .post("/scrapyrt", {
        spider_name: "Chapter",
        request: {
          url: this.$route.query.url
        }
      })
      .then(response => {
        if (response.data.status !== "ok") {
          this.$message({
            message: "网络错误",
            type: "warning"
          });
        } else {
          console.log(response);
          const result=response.data.items[0];
          this.content=result.content;
        }
      })
      .catch(() => {
        this.$message({
          message: "网络错误",
          type: "warning"
        });
      });
  }
};
</script>

<style scoped>
</style>