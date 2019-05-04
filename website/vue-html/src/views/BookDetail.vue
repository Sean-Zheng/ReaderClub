<template>
  <div id="book-detail">
    <div class="link-box">
      <el-breadcrumb separator=">">
        <el-breadcrumb-item>
          <router-link to="/">首页</router-link>
        </el-breadcrumb-item>
        <el-breadcrumb-item>
          <router-link to="#">{{book_type}}</router-link>
        </el-breadcrumb-item>
        <el-breadcrumb-item>{{name}}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <div class="message">
      <div class="img-box">
        <img :src="image_url" :alt="name" width="140" height="175">
      </div>
      <div class="desc-box">
        <h1>{{name}}</h1>
        <p>作&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;者：{{author}}</p>
        <p>状&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;态：{{status}}</p>
        <p>最后更新：{{update_time}}</p>
        <p>
          最新章节：
          <router-link :to="{name:'chapter',query:{url:latest_chapter_url}}">{{latest_chapters}}</router-link>
        </p>
        <div class="intro">
          <p>{{description}}</p>
        </div>
      </div>
    </div>
    <ul class="catalogs">
      <li
        v-for="item in catalogs"
        :key="item.link"
      >
        <router-link :to="{name:'chapter',query:{link:item.link}}">{{ item.text }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "book-detail",
  data() {
    return {
      name: "",
      author: "",
      status: "",
      book_type: "",
      update_time: "",
      latest_chapters: "",
      latest_chapter_url: "",
      image_url: "",
      description: "",
      catalogs: []
    };
  },
  created() {
    axios
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
  }
};
</script>

<style scoped>
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
</style>