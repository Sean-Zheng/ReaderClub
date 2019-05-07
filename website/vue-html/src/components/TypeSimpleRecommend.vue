<template>
  <div class="type-simple-recommend">
    <router-link :to="{name:'detail',query:{url:SimpleItem.link}}">{{SimpleItem.name}}</router-link>
    <span>-</span>
    <router-link
      :to="{name:'search',query:{keyword:SimpleItem.author}}"
      style="color:rgba(52, 73, 94,0.6)"
    >
      <span>{{SimpleItem.author}}</span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "type-simple-recommend",
  props: {
    SimpleItem: {
      type: Object,
      default: null,
      required: true
    }
  }
};
</script>

<style scoped>
.type-simple-recommend {
  width: 50%;
  float: left;
  padding: 5px 10px;
  box-sizing: border-box;
  border-bottom: 1px dotted rgba(124, 153, 204, 0.8);
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}
.type-simple-recommend a {
  text-decoration: none;
  color: rgb(124, 153, 204);
}
.type-simple-recommend a:hover {
  color: #c0392b;
  text-decoration: underline;
}
</style>