<template>
  <div v-if="btnFlag" class="iconfont icon-top to-top" @click="toTop()"></div>
</template>

<script>
export default {
  name: "to-top",
  data() {
    return {
      btnFlag: false
    };
  },
  methods: {
    toTop() {
      let that = this;
      let timer = setInterval(() => {
        let ispeed = Math.floor(-that.scrollTop / 5);
        document.getElementById("app").scrollTop = that.scrollTop + ispeed;
        if (that.scrollTop === 0) {
          clearInterval(timer);
        }
      }, 16);
    },
    scrollToTop() {
      let that = this;
      let scrollTop = document.getElementById("app").scrollTop;
      that.scrollTop = scrollTop;
      if (that.scrollTop > 60) {
        that.btnFlag = true;
      } else {
        that.btnFlag = false;
      }
    }
  },
  mounted() {
    document.getElementById("app").addEventListener("scroll", this.scrollToTop);
  },
  destroyed() {
    document
      .getElementById("app")
      .removeEventListener("scroll", this.scrollToTop);
  }
};
</script>

<style scoped>
.to-top {
  width: 60px;
  height: 60px;
  position: fixed;
  font-size: 30px;
  text-align: center;
  line-height: 60px;
  cursor: pointer;
  border: 1px solid #d8d8d8;
}
</style>