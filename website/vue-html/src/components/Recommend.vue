<template>
  <div id="recommend">
    <el-carousel height="300px">
      <el-carousel-item v-for="item in this.$store.getters.getHomeList" :key="item.name">
        <div class="item">
          <div class="img-box">
            <router-link :to="{name:'detail',query:{url:item.link}}">
              <img :src="item.image_url" :alt="item.name" width="120" height="150">
            </router-link>
          </div>
          <dl class="message-box">
            <dt>
              <router-link :to="{name:'detail',query:{url:item.link}}">{{item.name}}</router-link>
              <span>{{item.author}}</span>
            </dt>
            <dd>{{item.description}}</dd>
          </dl>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: "recommend"
};
</script>

<style scoped>
#recommend {
  width: 600px;
}
.item {
  background-color: #f7f6f2;
  height: 300px;
  padding: 0 50px;
  border: 1px solid #e6e6e6;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.message-box {
  width: 350px;
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
}
.message-box dd {
  margin: 0;
  margin: 20px;
  height: 150px;
  overflow: hidden;
}
</style>