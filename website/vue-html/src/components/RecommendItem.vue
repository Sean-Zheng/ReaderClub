<template>
  <div class="recommend-item">
    <div class="box">
      <div class="name-box">
        <router-link :to="{name:'detail',query:{url:Item.book_url}}">{{Item.book_name}}</router-link>
      </div>

      <div class="author-box">
        <router-link :to="{name:'search',query:{keyword:Item.book_author}}">
          <span>{{Item.book_author}}</span>
        </router-link>
      </div>
    </div>
    <p class="des">{{Item.book_description}}</p>
  </div>
</template>

<script>
export default {
  props: {
    Item: {
      type: Object,
      default: null,
      required: true
    }
  }
};
</script>

<style scoped>
.recommend-item {
  border-bottom: 1px dotted #e6e6e6;
}
.box {
  display: flex;
  justify-content: space-between;
}
.name-box,
.author-box {
  padding: 0 15px;
}
.recommend-item >>> a {
  color: rgb(124, 153, 204);
  text-decoration: none;
}
.recommend-item >>> a:hover {
  color: #c0392b;
}
.des {
  margin: 5px 0 10px;
  height: 62px;
  overflow: hidden;
  font-size: 12px;
  color: rgba(52, 73, 94, 0.6);
}
</style>

