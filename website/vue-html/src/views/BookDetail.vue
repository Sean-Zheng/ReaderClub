<template>
  <div class="book-detail" v-loading.fullscreen.lock="loading">
    <div class="link-box">
      <el-breadcrumb separator=">">
        <el-breadcrumb-item>
          <router-link to="/">首页</router-link>
        </el-breadcrumb-item>
        <el-breadcrumb-item>
          <router-link :to="{path:`/type/${book_type}`}">{{book_type}}</router-link>
        </el-breadcrumb-item>
        <el-breadcrumb-item>{{name}}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="message">
      <div class="img-box">
        <img :src="image_url" :alt="name" width="140" height="175" @error="imgDefault($event)">
      </div>
      <div class="desc-box">
        <h1>{{name}}</h1>
        <p>作&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;者：{{author}}</p>
        <p>状&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;态：{{status}}</p>
        <p>最后更新：{{update_time}}</p>
        <p>
          最新章节：
          <router-link
            :to="{name:'chapter',query:{link:latest_chapter_url}}"
            style="color:rgb(124, 153, 204);"
          >{{latest_chapters}}</router-link>
        </p>
        <div class="intro">
          <p>{{description}}</p>
        </div>
      </div>
    </div>
    <div class="opration-box">
      <el-button @click="addToShelf()">加入书架</el-button>
      <el-button @click="readBook()" type="primary">开始阅读</el-button>
    </div>

    <div class="commend-box">
      <comment-add :name="name" :author="author" @commentAddSuccess="initComments"></comment-add>
      <div class="comment-list">
        <p v-if="comments.length===0">暂无评论</p>
        <comment-item v-else v-for="item in comments" :Item="item" :key="item.comment_id"></comment-item>
      </div>
    </div>
    <to-top/>
  </div>
</template>

<script>
import axios from "axios";
import ToTop from "@/components/ToTop";
import CommentAdd from "@/components/CommentAdd";
import CommentItem from "@/components/CommentItem";
export default {
  name: "book-detail",
  data() {
    return {
      loading: true,
      name: "",
      author: "",
      status: "",
      book_type: "",
      update_time: "",
      latest_chapters: "",
      latest_chapter_url: "",
      image_url: "",
      description: "",
      catalogs: [],
      comments: []
    };
  },
  methods: {
    imgDefault(event) {
      this.image_url = require("@/assets/nocover.jpg");
    },
    addToShelf() {
      axios
        .post(
          "/flask/book/add",
          {
            name: this.name,
            author: this.author,
            description: this.description,
            source_url: this.$route.query.url,
            book_type: this.book_type
          },
          {
            headers: {
              Authorization: this.$store.getters.getToken
            }
          }
        )
        .then(res => {
          if (res.data.status === 212) {
            this.$message({
              message: "添加成功",
              type: "success"
            });
          } else {
            this.$message({
              message: "网络错误",
              type: "warning"
            });
          }
        })
        .catch(() => {
          //请登录
          this.$message({
            message: "请登陆账号...",
            type: "warning"
          });
          this.$router.push("/login");
        });
    },
    readBook() {
      this.$router.push({
        name: "chapter",
        query: { link: this.catalogs[0].link }
      });
    },
    initMessage() {
      return axios
        .post("/scrapyrt", {
          spider_name: "Catalog",
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
            this.loading = false;
            const msg = response.data.items[0];
            this.name = msg.name;
            this.author = msg.author;
            this.status = msg.status;
            this.book_type = msg.book_type;
            this.update_time = msg.update_time;
            this.latest_chapters = msg.latest_chapters;
            this.latest_chapter_url = msg.latest_chapter_url;
            this.image_url = msg.image_url;
            this.description = msg.description;
            this.catalogs = msg.catalogs;
          }
        })
        .catch(() => {
          this.$message({
            message: "网络错误",
            type: "warning"
          });
        });
    },
    initComments() {
      axios
        .post("/flask/comment/book/list", {
          name: this.name,
          author: this.author
        })
        .then(res => {
          this.comments = res.data.list;
        });
    }
  },
  components: {
    ToTop,
    CommentAdd,
    CommentItem
  },
  created() {
    this.initMessage().then(() => {
      this.initComments();
    });
  }
};
</script>

<style scoped>
.book-detail {
  padding: 10px 150px;
}
.color-box {
  background-color: #f7f6f2;
}
.link-box {
  margin: 20px 70px;
}
.link-box a {
  text-decoration: none;
  color: #2c3e50;
}
.message {
  display: flex;
  justify-content: space-around;
  margin: 0 70px;
  border: 3px solid #e5e5e5;
  border-bottom-width: 0;
  color: #2c3e50;
}
.img-box {
  padding: 20px;
  margin: 30px;
  align-self: center;
}
.desc-box {
  margin: 10px 30px;
}
.desc-box > p {
  display: inline-block;
  width: 50%;
  font-size: 15px;
  margin: 5px 0 0;
}
.desc-box p a {
  text-decoration: none;
  color: #2c3e50;
}
.desc-box p a:hover {
  text-decoration: underline;
  color: #c0392b;
}
.intro {
  margin-top: 30px;
  border-top: 1px dotted rgb(166, 211, 232);
  font-size: 14px;
}
.catalogs {
  margin: 20px 70px;
  overflow: hidden;
}
.catalogs > li {
  list-style: none;
  width: 33.33%;
  height: 45px;
  line-height: 45px;
  padding-left: 30px;
  box-sizing: border-box;
  float: left;
  margin: 0;
  font-size: 14px;
  border-bottom: 1px solid #ebebeb;
}
.catalogs > li > a {
  text-decoration: none;
  color: #2c3e50;
}
.catalogs > li > a:hover {
  text-decoration: underline;
  color: #c0392b;
}
.comment-list {
  margin: 50px auto;
  width: 1000px;
}
.comment-list > p {
  text-align: center;
}
.opration-box {
  display: flex;
  justify-content: center;
}
.to-top {
  bottom: 50px;
  right: 100px;
}
</style>