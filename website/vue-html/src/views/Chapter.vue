<template>
  <div id="chapter">
    <page
      :chapter_title="title"
      :content="content"
      :catalogs_url="catalog_url"
      :previous="previous_chapter"
      :next="next_chapter"
      v-loading.fullscreen.lock="loading"
      element-loading-background="rgba(0,0,0,0)"
    ></page>
  </div>
</template>

<script>
import axios from "axios"
import Page from "@/components/Page"
export default {
  name: "chapter",
  data() {
    return {
      loading: true,
      title: "",
      previous_chapter: "",
      next_chapter: "",
      catalog_url: "",
      content: ""
    };
  },
  components: {
    Page
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      axios
        .post("/scrapyrt", {
          spider_name: "Chapter",
          request: {
            url: this.$route.query.link
          }
        })
        .then(response => {
          if (response.data.status !== "ok") {
            //爬虫爬取失败
            this.$message({
              message: "网络错误",
              type: "warning"
            });
          } else if (response.data.errors) {
            //爬虫参数出错
            alert('aa');
            this.$router.push({
              name: "detail",
              query: { url: this.$route.query.link }
            });
          } else {
            //成功爬取
            this.loading = false;
            const result = response.data.items[0];
            this.title = result.title;
            this.previous_chapter = result.previous_chapter;
            this.next_chapter = result.next_chapter;
            this.catalog_url = result.catalog_url;
            this.content = result.content;
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
  watch: {
    $route(to, from) {
      this.getData();
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
  }
};
</script>

<style scoped>
</style>