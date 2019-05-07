<template>
  <div class="type-view" v-loading.fullscreen.lock="loading">
    <type-navigation @routeChange="getWebData"/>
    <div class="detail">
      <type-detail-recommend v-for="item in detail_list" :key="item.link" :DetailItem="item"></type-detail-recommend>
    </div>
    <hr>
    <div>
      <type-simple-recommend v-for="item in simple_list" :key="item.link" :SimpleItem="item"></type-simple-recommend>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TypeNavigation from "@/components/TypeNavigation";
import TypeDetailRecommend from "@/components/TypeDetailRecommend";
import TypeSimpleRecommend from "@/components/TypeSimpleRecommend";
export default {
  name: "type-view",
  data() {
    return {
      loading: true,
      detail_list: [],
      simple_list: []
    };
  },
  methods: {
    getWebData() {
      this.loading = true;
      axios
        .post("/scrapyrt", {
          spider_name: "Classification",
          request: {
            url: this.$store.state.typeLink[this.$route.params.typename]
          }
        })
        .then(response => {
          if (response.data.status !== "ok") {
            //爬虫爬取失败
            this.$message({
              message: "网络错误",
              type: "warning"
            });
          } else {
            //成功爬取
            this.loading = false;
            const result = response.data.items[0];
            this.detail_list = result.detail_list;
            this.simple_list = result.simple_list;
          }
        })
        .catch(() => {
          //网络出错
          this.$message({
            message: "网络错误",
            type: "warning"
          });
        });
    }
  },
  created() {
    this.getWebData();
  },
  components: {
    TypeNavigation,
    TypeDetailRecommend,
    TypeSimpleRecommend
  }
};
</script>

<style scoped>
.detail {
  overflow: auto;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}
</style>