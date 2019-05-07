<template>
  <div id="page">
    <div class="side" :class="getPageColor()">
      <ul>
        <!-- 目录 -->
        <el-popover
          v-model="showCatalogs"
          placement="right-start"
          trigger="click"
          @show="getCatalogs"
        >
          <div
            v-loading="catalogs_loading"
            element-loading-background="rgba(255,255,255,0.3)"
            class="catalog-box"
            :class="getSideColor()"
          >
            <h3>目录</h3>
            <dl>
              <dd v-for="item in catalogs" :key="item.link" @click="showCatalogs=false">
                <router-link :to="{name:'chapter',query:{link:item.link}}">{{ item.text }}</router-link>
              </dd>
            </dl>
          </div>
          <li slot="reference">
            <em class="iconfont icon-mulu"></em>
            <span>目录</span>
          </li>
        </el-popover>
        <!-- 设置 -->
        <el-popover
          placement="right-start"
          trigger="click"
          v-model="showSetting"
          @hide="resetTheme()"
        >
          <div class="setting-box" :class="getSideColor()">
            <dl class="color-list">
              <dd :class="theme==='default'?'el-icon-check':''" @click="theme='default'"></dd>
              <dd :class="theme==='yellow'?'el-icon-check':''" @click="theme='yellow'"></dd>
              <dd :class="theme==='green'?'el-icon-check':''" @click="theme='green'"></dd>
              <dd :class="theme==='blue'?'el-icon-check':''" @click="theme='blue'"></dd>
              <dd :class="theme==='gray'?'el-icon-check':''" @click="theme='gray'"></dd>
              <dd :class="theme==='black'?'el-icon-check':''" @click="theme='black'"></dd>
            </dl>
            <div>
              <el-button @click="showSetting=false">取消</el-button>
              <el-button type="primary" @click="changeColor(theme)">确认</el-button>
            </div>
          </div>
          <li slot="reference">
            <em class="iconfont icon-shezhi1"></em>
            <span>设置</span>
          </li>
        </el-popover>
        <li @click="addToShelf()">
          <em class="iconfont icon-shujia"></em>
          <span v-if="isExist">已在书架</span>
          <span v-else>书架</span>
        </li>
        <!-- 书签 -->
        <el-popover placement="right-start" trigger="click">
          <li slot="reference">
            <em class="iconfont icon-icon--"></em>
            <span>书签</span>
          </li>
        </el-popover>
        <!-- 评论 -->
        <el-popover placement="right-start" width="200" trigger="click">
          <li slot="reference">
            <em class="iconfont icon-pinglun"></em>
            <span>评论</span>
          </li>
        </el-popover>
      </ul>
    </div>
    <div class="main-box" :class="getPageColor()">
      <div class="title-box">
        <h3>{{chapter_title}}</h3>
      </div>
      <p v-html="content"></p>
    </div>
    <div class="link-box" :class="getPageColor()">
      <router-link :to="{name:'chapter',query:{link:previous}}">上一章</router-link>
      <router-link :to="{name:'detail',query:{url:catalogs_url}}">目录</router-link>
      <router-link :to="{name:'chapter',query:{link:next}}">下一章</router-link>
    </div>
    <to-top :class="getPageColor()"/>
  </div>
</template>

<script>
import axios from "axios";
import ToTop from "@/components/ToTop";
import { mapGetters, mapActions } from "vuex";
export default {
  name: "page",
  data() {
    return {
      theme: this.$store.getters.getTheme,
      showCatalogs: false,
      showSetting: false,
      loadding: true,
      catalogs_loading: true,
      name: "",
      author: "",
      catalogs: [],
    };
  },
  computed: {
    ...mapGetters(["getBookList", "getLoginResult"]),
    isExist() {
      //判断是否已经登陆
      if (this.getLoginResult) {
        let result = this.getBookList.find(
          item => item.name === this.name && item.author === this.author
        );
        return result === undefined ? false : true;
      } else {
        return false;
      }
    }
  },
  watch: {
    catalogs_url(newval, oldval) {
      this.getCatalogs();
    }
  },
  methods: {
    //更换背景颜色
    changeColor(themeStr) {
      this.$store.commit("setTheme", themeStr);
      this.showSetting = false;
    },
    resetTheme() {
      this.theme = this.$store.getters.getTheme;
    },
    getPageColor() {
      return `${this.$store.getters.getTheme}-page ${
        this.$store.getters.getTheme
      }-font`;
    },
    getSideColor() {
      return `${this.$store.getters.getTheme}-side`;
    },
    getCatalogs() {
      axios
        .post("/scrapyrt", {
          spider_name: "Catalog",
          request: {
            url: this.catalogs_url
          }
        })
        .then(response => {
          if (response.data.status !== "ok") {
            this.$message({
              message: "网络错误!",
              type: "warning"
            });
          } else {
            this.catalogs_loading = false;
            const msg = response.data.items[0];
            this.catalogs = msg.catalogs;
            this.name = msg.name;
            this.author = msg.author;
            this.description = msg.description;
            this.book_type = msg.book_type;
          }
        })
        .catch(() => {
          this.$message({
            message: "网络错误?",
            type: "warning"
          });
        });
    },
    addToShelf() {
      if (this.isExist) {
        return;
      }
      axios
        .post(
          "/flask/book/add",
          {
            name: this.name,
            author: this.author,
            description: this.description,
            source_url: this.catalogs_url,
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
            this.isExist = true;
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
    ...mapActions(["getBookListAction"])
  },
  props: {
    chapter_title: {
      type: String,
      default: "",
      required: true
    },
    content: {
      type: String,
      default: "",
      required: true
    },
    catalogs_url: {
      type: String,
      default: "",
      required: true
    },
    previous: {
      type: String,
      default: "",
      required: true
    },
    next: {
      type: String,
      default: "",
      required: true
    }
  },
  created() {
    this.getBookListAction();
  },
  mounted() {
    document.getElementById("app").addEventListener("scroll", this.scrollToTop);
  },
  destroyed() {
    document
      .getElementById("app")
      .removeEventListener("scroll", this.scrollToTop);
  },
  components: {
    ToTop
  }
};
</script>

<style scoped>
.side {
  position: fixed;
}
.side > ul {
  margin: 0;
  padding: 0;
}
.side > ul li {
  width: 60px;
  height: 60px;
  text-align: center;
  list-style: none;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: center;
  user-select: none;
  border: 1px solid #d8d8d8;
}
.side > ul li:hover {
  color: #c0392b;
}
.side > ul li > span {
  padding-top: 3px;
  font-size: 12px;
}
.side > ul li > em {
  font-size: 20px;
}
.catalog-box {
  background-color: aliceblue;
  width: 650px;
  height: 750px;
}
.catalog-box > h3 {
  margin: 0;
  padding: 20px;
}
.catalog-box > dl {
  margin: 0;
  height: 650px;
  overflow-y: scroll;
}
.catalog-box > dl > dd {
  padding: 5px 0 5px 30px;
  margin: 0;
  width: 50%;
  box-sizing: border-box;
  float: left;
}
.catalog-box > dl > dd > a {
  text-decoration: none;
  color: #2c3e50;
}
.catalog-box > dl > dd > a:hover {
  text-decoration: underline;
  color: #c0392b;
}
.setting-box {
  width: 500px;
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.color-list {
  margin: 0;
  display: flex;
  justify-content: space-around;
  overflow: auto;
}
.color-list > dd {
  width: 45px;
  height: 45px;
  font-size: 25px;
  line-height: 45px;
  text-align: center;
  margin: 0;
  border-radius: 50%;
  color: #ed4259;
  border: 1px solid #ed4259;
  cursor: pointer;
}
.color-list > dd:nth-child(1) {
  background-image: url("../assets/page0.png");
}
.color-list > dd:nth-child(2) {
  background-image: url("../assets/page1.png");
}
.color-list > dd:nth-child(3) {
  background-image: url("../assets/page2.png");
}
.color-list > dd:nth-child(4) {
  background-image: url("../assets/page3.png");
}
.color-list > dd:nth-child(5) {
  background-image: url("../assets/page4.png");
}
.color-list > dd:nth-child(6) {
  background-image: url("../assets/page5.png");
}
.setting-box > div {
  display: flex;
  justify-content: center;
  padding-top: 20px;
}
.title-box > h3 {
  margin: 0;
  text-align: center;
  font-size: 24px;
  font-weight: initial;
}
.main-box {
  width: 900px;
  margin: 0 auto;
  padding: 60px;
  border: 1px solid #d8d8d8;
}
.main-box > p {
  user-select: none;
  font-size: 22px;
  line-height: 35px;
  font-weight: lighter;
}
.link-box {
  width: 1020px;
  height: 70px;
  margin: 30px auto 0;
  border: 1px solid #d8d8d8;
  display: flex;
  justify-content: space-around;
}
.link-box > a {
  text-decoration: none;
  text-align: center;
  line-height: 70px;
  width: 33%;
  display: inline-block;
  border: 1px solid #d8d8d8;
  color: #2c3e50;
}
.link-box > a:hover {
  background-color: rgba(0, 0, 0, 0.1);
}
.to-top {
  bottom: 50px;
  left: 1270px;
}
/*
主题类
*/
.default-page {
  background-image: url("../assets/page0.png");
}
.yellow-page {
  background-image: url("../assets/page1.png");
}
.green-page {
  background-image: url("../assets/page2.png");
}
.blue-page {
  background-image: url("../assets/page3.png");
}
.gray-page {
  background-image: url("../assets/page4.png");
}
.black-page {
  background-image: url("../assets/page5.png");
}

.default-side {
  background-image: url("../assets/side0.png");
}
.yellow-side {
  background-image: url("../assets/side1.png");
}
.green-side {
  background-image: url("../assets/side2.png");
}
.blue-side {
  background-image: url("../assets/side3.png");
}
.gray-side {
  background-image: url("../assets/side4.png");
}
.black-side {
  background-image: url("../assets/side5.png");
}
.default-font {
  color: #262626;
}
.yellow-font {
  color: #3b3a37;
}
.green-font {
  color: #262626;
}
.blue-font {
  color: #262626;
}
.gray-font {
  color: #262626;
}
.black-font {
  color: #666;
}
</style>

<style>
.el-popover {
  padding: 1px;
}
</style>
