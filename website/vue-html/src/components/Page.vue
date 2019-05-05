<template>
  <div id="page" @contextmenu.prevent>
    <div class="side">
      <ul ref="list">
        <el-popover
          v-model="showCatalogs"
          placement="right-start"
          trigger="click"
          @show="getCatalogs"
        >
          <div ref="catalog" v-loading="catalogs_loading" class="catalog-box">
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
        <el-popover placement="right-start" width="200" trigger="click">
          <div class="setting-box">

          </div>
          <li slot="reference">
            <em class="iconfont icon-shezhi1"></em>
            <span>设置</span>
          </li>
        </el-popover>
        <el-popover placement="right-start" width="200" trigger="click">
          <li slot="reference">
            <em class="iconfont icon-shujia"></em>
            <span>书架</span>
          </li>
        </el-popover>
        <el-popover placement="right-start" width="200" trigger="click">
          <li slot="reference">
            <em class="iconfont icon-icon--"></em>
            <span>书签</span>
          </li>
        </el-popover>
        <el-popover placement="right-start" width="200" trigger="click">
          <li slot="reference">
            <em class="iconfont icon-pinglun"></em>
            <span>评论</span>
          </li>
        </el-popover>
      </ul>
    </div>
    <div ref="page" class="main-box">
      <div class="title-box">
        <h3 ref="chapter_title">{{chapter_title}}</h3>
      </div>
      <p ref="content" v-html="content"></p>
    </div>
    <div ref="link_box" class="link-box">
      <router-link :to="{name:'chapter',query:{link:previous}}">上一章</router-link>
      <router-link :to="{name:'detail',query:{url:catalogs_url}}">目录</router-link>
      <router-link :to="{name:'chapter',query:{link:next}}">下一章</router-link>
    </div>
    <div class="iconfont icon-top top" @click="toTop"></div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "page",
  data() {
    return {
      showCatalogs: false,
      loadding: true,
      catalogs_loading: true,
      catalogs: [],
      black_class:{
         background: `url(${require("../assets/body5.png")})`
      },
      theme: {
        default: {
          background: `url(${require("../assets/body0.png")})`,
          pages: `url(${require("../assets/page0.png")})`,
          font: "#262626"
        },
        yellow: {
          background: `url(${require("../assets/body1.png")})`,
          pages: `url(${require("../assets/page1.png")})`,
          font: "#3b3a37"
        },
        green: {
          background: `url(${require("../assets/body2.png")})`,
          pages: `url(${require("../assets/page2.png")})`,
          font: "#262626"
        },
        blue: {
          background: `url(${require("../assets/body3.png")})`,
          pages: `url(${require("../assets/page3.png")})`,
          font: "#262626"
        },
        graty: {
          background: `url(${require("../assets/body4.png")})`,
          pages: `url(${require("../assets/page4.png")})`,
          font: "#262626"
        },
        black: {
          background: `url(${require("../assets/body5.png")})`,
          pages: `url(${require("../assets/page5.png")})`,
          font: "#666"
        }
      }
    };
  },
  methods: {
    //更换背景颜色
    changeColor(themeStr) {
      this.$refs.catalog.style.backgroundImage = this.theme[themeStr].pages;
      this.$refs.list.style.backgroundImage = this.theme[themeStr].pages;
      this.$refs.chapter_title.style.color = this.theme[themeStr].font;
      this.$refs.content.style.color = this.theme[themeStr].font;
      this.$refs.page.style.backgroundImage = this.theme[themeStr].pages;
      this.$refs.link_box.style.backgroundImage = this.theme[themeStr].pages;
      document.body.style.backgroundImage = this.theme[themeStr].background;
      document.getElementById("navigation").style.backgroundColor =
        "rgba(255,255,255,0.4)";
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
              message: "网络错误",
              type: "warning"
            });
          } else {
            this.catalogs_loading = false;
            const msg = response.data.items[0];
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
    toTop() {
      let that = this;
      let timer = setInterval(() => {
        let ispeed = Math.floor(-that.scrollTop / 5);
        document.documentElement.scrollTop = document.body.scrollTop =
          that.scrollTop + ispeed;
        if (that.scrollTop === 0) {
          clearInterval(timer);
        }
      }, 16);
    },
    scrollToTop() {
      let that = this;
      let scrollTop =
        window.pageYOffset ||
        document.documentElement.scrollTop ||
        document.body.scrollTop;
      that.scrollTop = scrollTop;
      if (that.scrollTop > 60) {
        that.btnFlag = true;
      } else {
        that.btnFlag = false;
      }
    }
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
  mounted() {
    this.changeColor("default");
    window.addEventListener("scroll", this.scrollToTop);
  },
  destroyed() {
    window.removeEventListener("scroll", this.scrollToTop);
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
.setting-box{
  width: 650px;
  height: 200px;
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
.link-box{
  width: 1020px;
  height: 70px;
  margin: 30px auto 0;
  border: 1px solid #d8d8d8;
  display: flex;
  justify-content: space-around;
}
.link-box>a{
  text-decoration: none;
  text-align: center;
  line-height: 70px;
  width: 33%;
  display: inline-block;
  border: 1px solid #d8d8d8;
  color: #2c3e50;
}
.link-box>a:hover{
  background-color: rgba(0,0,0,0.1);
}
.top {
  width: 60px;
  height: 60px;
  position: fixed;
  font-size: 30px;
  text-align: center;
  line-height: 60px;
  bottom: 50px;
  left: 1270px;
  cursor: pointer;
  border: 1px solid #d8d8d8;
}
</style>

<style>
.el-popover {
  padding: 0;
}
</style>
