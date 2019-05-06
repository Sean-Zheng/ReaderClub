<template>
  <div class="book-item">
    <div class="item">
      <div class="img-box">
        <router-link :to="{name:'detail',query:{url:item.source_url}}">
          <img
            :src="item.image_url"
            :alt="item.name"
            width="120"
            height="150"
            @error="imgDefault($event)"
          >
        </router-link>
      </div>
      <dl class="message-box">
        <dt>
          <router-link :to="{name:'detail',query:{url:item.source_url}}">{{item.name}}</router-link>
          <span>
            <router-link :to="{name:'search',query:{keyword:item.author}}">{{item.author}}</router-link>
          </span>
          <span>{{item.book_type}}</span>
        </dt>
        <dd class="des">{{item.description}}</dd>
        <dd class="chapter">
          最新更新：
          <router-link
            :to="{name:'chapter',query:{link:item.latest_chapter_url}}"
          >{{item.latest_chapters}}</router-link>
        </dd>
        <dd class="time-box">最后更新：{{item.update_time}}</dd>
      </dl>
    </div>
  </div>
</template>

<script>
export default {
  name: "book-item",
  props: {
    item: {
      type: Object,
      default: null,
      required: true
    }
  },
  methods: {
    imgDefault(event) {
      this.item.image_url = require("@/assets/nocover.jpg");
    }
  }
};
</script>

<style scoped>
.item {
  background-color: #f7f6f2;
  height: 220px;
  padding: 0 50px;
  border: 1px solid #e6e6e6;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.message-box {
  width: 600px;
}
.message-box a {
  text-decoration: none;
  color: rgb(124, 153, 204);
}
.message-box dt {
  border-bottom: 1px dotted rgb(166, 211, 232);
  padding: 0 20px 5px;
}
.message-box dt span {
  float: right;
  padding: 0 10px;
}
.des {
  margin: 20px;
  height: 70px;
}
.chapter {
  float: left;
}
.time-box {
  margin: 0;
  float: right;
}
</style>