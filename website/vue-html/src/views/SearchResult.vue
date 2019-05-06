<template>
  <div>
    <p>“{{keyword}}”搜索结果:</p>
    <book-item :item="item" v-for="item in results" :key="item.source_url"></book-item>
    <div class="result-list" v-loading.fullscreen.lock="loading">
      <el-pagination
        v-if="page_count>1"
        background
        layout="prev, pager, next"
        :total="page_count*10"
        @current-change="currentChange"
      ></el-pagination>
    </div>
    <to-top/>
  </div>
</template>

<script>
import axios from "axios";
import BookItem from "@/components/BookItem";
import ToTop from "@/components/ToTop";
export default {
  data() {
    return {
      loading: true,
      results: [],
      current: 1,
      page_count: 1
    };
  },
  computed: {
    keyword() {
      return this.$route.query.keyword;
    }
  },
  methods: {
    searchBooks() {
      return axios
        .post("/scrapyrt", {
          spider_name: "Search",
          request: {
            url:
              this.current == 1
                ? `https://www.biduo.cc/search.php?keyword=${this.keyword}`
                : `https://www.biduo.cc/search.php?keyword=${
                    this.keyword
                  }&page=${this.current}`
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
            this.loading = false;
            this.results = response.data.items;
            this.page_count = response.data.items[0].page_count;
          }
        });
    },
    currentChange(val) {
      this.current = val;
      this.searchBooks();
      this.loading = true;
      document.getElementById("app").scrollTop = 0;
    }
  },
  components: {
    BookItem,
    ToTop
  },
  created() {
    this.searchBooks();
  },
  watch: {
    $route(to, from) {
      if (to.path === "/search") {
        this.loading = true;
        if (to.query.keyword !== from.query.keyword) {
          this.current = 1;
        }
        this.searchBooks();
      }
    }
  }
};
</script>

<style scoped>
.el-pagination {
  margin: 30px;
  display: flex;
  justify-content: center;
}
.to-top {
  bottom: 50px;
  right: 100px;
}
</style>