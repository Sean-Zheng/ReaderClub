<template>
  <div class="type-view" v-loading.fullscreen.lock="loading">
    <type-navigation @routeChange="getWebData"/>
    <p>{{this.$route.params.typename}}</p>
    <p>{{this.$store.state.typeLink['玄幻魔法']}}</p>
    <ul>
      <li v-for="item in detail_list" :key="item.link">
        <router-link :to="{name:'detail',query:{url:item.link}}">{{ item.name }}</router-link>-
        <router-link :to="{name:'search',query:{keyword:item.author}}">{{ item.author }}</router-link>
        <p>{{item.description}}</p>
      </li>
    </ul>
    <hr>
    <ul>
      <li v-for="item in simple_list" :key="item.link">
        <router-link :to="{name:'detail',query:{url:item.link}}">{{ item.name }}</router-link>-
        <router-link :to="{name:'search',query:{keyword:item.author}}">{{ item.author }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import TypeNavigation from "@/components/TypeNavigation";
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
    TypeNavigation
  }
};
</script>

<style scoped>
</style>