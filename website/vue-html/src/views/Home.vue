<template>
  <div class="home">
    <div class="home-first">
      <div>
        <classification></classification>
      </div>
      <div>
        <recommend></recommend>
      </div>
      <div v-if="getLoginResult" class="recommend-item-box">
        <p style="text-align: center;margin:0 0 5px;">推荐列表</p>
        <recommend-item v-for="item in recommendList" :Item="item" :key="item.book_url"></recommend-item>
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
import RecommendItem from "../components/RecommendItem";
import { mapState,mapGetters, mapActions } from "vuex";
export default {
  name: "home",
  data () {
    return {
      url1:process.env.VUE_APP_SCRAPY_URL,
      url2:process.env.VUE_APP_FLASK_URL
    }
  },
  components: {
    Classification,
    Recommend,
    ClassificationRecommend,
    RecommendItem
  },
  computed: {
    ...mapState(["recommendList"]),
    ...mapGetters(["getLoginResult"])
  },
  methods: {
    ...mapActions(["recommendAction"])
  },
  created() {
    this.recommendAction();
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
.home {
  padding: 10px 150px;
}
.recommend-item-box{
  background-color: #f7f6f2;
  border: 1px solid #e6e6e6;
  box-sizing: border-box;
  padding: 5px;
}
.home-first {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.recommend-item-box{
  width:300px;
}
.home-second {
  overflow: auto;
  margin: 30px 0;
}
</style>
