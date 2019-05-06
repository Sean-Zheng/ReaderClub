<template>
  <div class="type-navigation">
    <ul class="link-list">
      <li>
        <router-link :to="{path:'/type/玄幻魔法'}">
          <span class="iconfont icon-xuanhuan"></span>玄幻魔法
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/武侠修真'}">
          <span class="iconfont icon-wuxia"></span>武侠修真
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/都市言情'}">
          <span class="iconfont icon-dushi"></span>都市言情
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/历史军事'}">
          <span class="iconfont icon-junshi"></span>历史军事
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/网游动漫'}">
          <span class="iconfont icon-erciyuan"></span>网游动漫
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/科幻小说'}">
          <span class="iconfont icon-kehuan"></span>科幻小说
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/恐怖灵异'}">
          <span class="iconfont icon-lingyi"></span>恐怖灵异
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/其他小说'}">
          <span class="iconfont icon-other"></span>其他小说
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "type-navigation",
  watch: {
    $route(to, from) {
      if (to.params.typename !== from.params.typename) {
        this.$emit("routeChange");
      }
    }
  }
};
</script>

<style scoped>
.link-list {
  width: 1120px;
  margin: 0 auto;
  padding: 0;
  overflow: auto;
  display: flex;
  justify-content: center;
  background-color: rgba(189, 195, 199, 0.4);
}
.link-list > li {
  text-align: center;
  list-style: none;
  width: 110px;
  height: 50px;
  float: left;
  line-height: 50px;
  cursor: pointer;
  margin: 0 10px;
  border: 1px solid #e6e6e6;
}
.link-list > li > a {
  user-select: none;
  color: #2c3e50;
  text-decoration: none;
}
.link-list > li:hover > a {
  color: #ed4259;
}
.link-list > li span {
  margin-right: 10px;
}
</style>