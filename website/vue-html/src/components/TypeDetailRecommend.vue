<template>
  <div class="type-detail-recommend">
    <div class="img-box">
      <router-link :to="{name:'detail',query:{url:DetailItem.link}}">
        <img
          :src="DetailItem.image_url"
          width="67"
          height="82"
          :alt="DetailItem.name"
          @error="imgDefault($event)"
        >
      </router-link>
    </div>
    <div class="intro">
      <router-link :to="{name:'detail',query:{url:DetailItem.link}}">
        <h4>{{DetailItem.name}}</h4>
      </router-link>
      <span>-</span>
      <router-link :to="{name:'search',query:{keyword:DetailItem.author}}">
        <span>{{DetailItem.author}}</span>
      </router-link>
      <p class="des">{{DetailItem.description}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "type-detail-recommend",
  props: {
    DetailItem: {
      type: Object,
      default: null,
      required: true
    }
  }
};
</script>

<style scoped>
.type-detail-recommend {
  margin: 10px;
  padding: 10px;
  overflow: auto;
  background-color: #f7f6f2;
  border: 1px solid #e6e6e6;
}
.type-detail-recommend a {
  color: rgb(124, 153, 204);
  text-decoration: none;
}

.type-detail-recommend a:hover {
  color: #c0392b;
  text-decoration: underline;
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
  display: inline;
}
.des {
  font-size: 12px;
}
</style>