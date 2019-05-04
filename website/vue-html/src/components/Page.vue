<template>
  <div id="page">
    <div>
      <div class="side">
        <span>ss</span>
      </div>
      <div ref="page" class="main-box">
        <div class="title-box">
          <h3 ref="chapter_title">{{chapter_title}}</h3>
        </div>
        <p ref="content" v-html="content"></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "page",
  data() {
    return {
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
      this.$refs.chapter_title.style.color = this.theme[themeStr].font;
      this.$refs.content.style.color = this.theme[themeStr].font;
      this.$refs.page.style.backgroundImage = this.theme[themeStr].pages;
      document.body.style.backgroundImage = this.theme[themeStr].background;
      document.getElementById('navigation').style.backgroundColor='rgba(255,255,255,0.4)';
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
    }
  },
  mounted() {
    this.changeColor("default");
  }
};
</script>

<style scoped>
.side {
  width: 60px;
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
  border:1px solid #d8d8d8;
}
.main-box > p {
  font-size: 22px;
  line-height: 35px;
  font-weight: lighter;
}
</style>