<template>
  <div class="classification-recommend">
    <h3>{{type_name}}</h3>
    <div class="first">
      <div class="img-box">
        <router-link :to="{name:'detail',query:{url:recommend_first.link}}">
          <img
            :src="recommend_first.image_url"
            width="67"
            height="82"
            :alt="recommend_first.name"
            @error="imgDefault($event)"
          >
        </router-link>
      </div>
      <div class="intro">
        <router-link :to="{name:'detail',query:{url:recommend_first.link}}">
          <h4>{{recommend_first.name}}</h4>
        </router-link>
        <p class="des">{{recommend_first.description}}</p>
      </div>
    </div>
    <ul class="list">
      <li v-for="item in recommend_list" :key="item.name">
        <router-link :to="{name:'detail',query:{url:item.link}}">{{item.name}}</router-link>
        <span>-</span>
        <router-link
          :to="{name:'search',query:{keyword:item.author}}"
          style="color:rgba(52, 73, 94,0.6)"
        >
          <span>{{item.author}}</span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "classification-recommend",
  props: {
    type_name: {
      type: String,
      default: "",
      required: true
    },
    recommend_first: {
      type: Object,
      default: null,
      required: true
    },
    recommend_list: {
      type: Array,
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
.classification-recommend {
  width: 350px;
  background-color: #f7f6f2;
  border: 1px solid #e6e6e6;
  margin: 10px;
  padding: 10px;
  float: left;
}
.classification-recommend a {
  text-decoration: none;
  color: rgb(124, 153, 204);
}
.classification-recommend a:hover {
  text-decoration: underline;
  color: #c0392b;
}
.classification-recommend > h3 {
  padding-left: 15px;
}
.first {
  overflow: auto;
}
.img-box {
  width: 80px;
  height: 110px;
  float: left;
  display: flex;
  align-items: center;
}
.intro {
  width: 270px;
  height: 110px;
  overflow: hidden;
  float: left;
}
.intro h4 {
  margin: 0;
}
.des {
  font-size: 12px;
}
.list {
  padding: 0;
  overflow: auto;
}
.list > li {
  list-style: none;
  width: 50%;
  float: left;
  padding: 5px 10px;
  box-sizing: border-box;
  border-bottom: 1px dotted rgba(124, 153, 204, 0.8);
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
.list > li > a {
  font-size: 12px;
}
</style>