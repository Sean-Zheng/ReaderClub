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
          <router-link to="#">{{latest_chapters}}</router-link>
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
        <router-link to="#">{{ item.text }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
/**
 * 
 * "name": "大道仙路",
    "author": "醉剑仙",
    "status": "连载中",
    "book_type": "武侠修真",
    "update_time": "2015-05-13 09:20:27",
    "latest_chapters": "第二十二章 入门",
    "latest_chapter_url": "https://www.biduo.cc/biquge/0_373/c40223.html",
    "image_url": "https://www.biduo.cc/files/article/image/0/373/373s.jpg",
    "description": "一个被逐出家族的少年，在一个优胜劣汰，适者生存的世界里，履历艰险，从练气，筑基，金丹，最终凝结元婴，且看主人公如何让在长生仙路上，披荆斩刺一路前行。\n\r\n\t\t\t\t各位书友要是觉得《大道仙路》还不错的话请不要忘记向您QQ群和微博里的朋友推荐哦！",
    "catalogs": [
        {
            "text": "第一章 逐出家族",
            "link": "https://www.biduo.cc/biquge/0_373/c39514.html"
        },
        {
            "text": "第二章 死里逃生",
            "link": "https://www.biduo.cc/biquge/0_373/c39515.html"
        },
 */
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