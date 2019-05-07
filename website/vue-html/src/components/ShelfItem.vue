<template>
  <div class="shelf-item">
    <div class="item">
      <dl class="message-box">
        <dt>
          <router-link :to="{name:'detail',query:{url:item.source_url}}">{{item.name}}</router-link>
          <span>
            <router-link :to="{name:'search',query:{keyword:item.author}}">{{item.author}}</router-link>
          </span>
          <span>{{item.book_type}}</span>
        </dt>
        <dd class="des">{{item.description}}</dd>
      </dl>
      <div class="user-operation">
        <el-button plain @click="toDetail()">书籍详情</el-button>
        <el-button type="primary" @click="removeFromShelf()">移出书架</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "shelf-item",
  props: {
    item: {
      type: Object,
      default: null,
      required: true
    }
  },
  methods: {
    imgDefault(event) {
      this.item.image_url = require("@/assets/nocover.jpg");
    },
    toDetail() {
      this.$router.push({
        name: "detail",
        query: { url: this.item.source_url }
      });
    },
    removeFromShelf() {
      this.$store
        .dispatch("removeBookAction", {
          name: this.item.name,
          author: this.item.author
        })
        .then(res => {
          if (res === 222) {
            this.$message({
              message: "删除成功",
              type: "success"
            });
          } else {
            this.$message({
              message: "网络错误",
              type: "warning"
            });
          }
        });
    }
  }
};
</script>

<style scoped>
.item {
  background-color: #f7f6f2;
  height: 220px;
  padding: 0 50px;
  border: 1px solid #e6e6e6;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.message-box {
  width: 600px;
}
.message-box a {
  text-decoration: none;
  color: rgb(124, 153, 204);
}
.message-box dt {
  border-bottom: 1px dotted rgb(166, 211, 232);
  padding: 0 20px 5px;
}
.message-box dt span {
  float: right;
  padding: 0 10px;
}
.des {
  margin: 20px;
  height: 70px;
}
.chapter {
  float: left;
}
.time-box {
  margin: 0;
  float: right;
}
.el-button {
  margin: 20px 0;
  display: block;
}
</style>