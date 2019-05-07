<template>
  <div id="home">
    <div class="home-first">
      <div>
        <classification></classification>
      </div>
      <div>
        <recommend></recommend>
      </div>
    </div>
    <div class="home-second">
      <div
        class="item"
        v-for="item in this.$store.getters.getClassificationList"
        :key="item.type_name"
      >
        <classification-recommend
          :type_name="item.type_name"
          :recommend_first="item.recommend_first"
          :recommend_list="item.recommend_list"
        ></classification-recommend>
      </div>
    </div>
  </div>
</template>

<script>
import Classification from "@/components/Classification";
import Recommend from "@/components/Recommend";
import ClassificationRecommend from "@/components/ClassificationRecommend";
export default {
  name: "home",
  components: {
    Classification,
    Recommend,
    ClassificationRecommend
  },
  created() {
    this.$store
      .dispatch("homeAction")
      .then(result => {
        if (result !== "ok") {
          this.$message({
            message: "网络错误",
            type: "warning"
          });
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
.home-first {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.home-second {
  overflow: auto;
  margin: 30px 0;
}
</style>
