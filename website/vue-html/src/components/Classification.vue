<template>
  <div id="classification">
    <ul>
      <li class="color-box">
        <router-link :to="{path:'/type/玄幻魔法'}">
          <span class="iconfont icon-xuanhuan"></span>玄幻魔法
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/武侠修真'}">
          <span class="iconfont icon-wuxia"></span>武侠修真
        </router-link>
      </li>
      <li class="color-box">
        <router-link :to="{path:'/type/都市言情'}">
          <span class="iconfont icon-dushi"></span>都市言情
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/历史军事'}">
          <span class="iconfont icon-junshi"></span>历史军事
        </router-link>
      </li>
      <li class="color-box">
        <router-link :to="{path:'/type/网游动漫'}">
          <span class="iconfont icon-erciyuan"></span>网游动漫
        </router-link>
      </li>
      <li>
        <router-link :to="{path:'/type/科幻小说'}">
          <span class="iconfont icon-kehuan"></span>科幻小说
        </router-link>
      </li>
      <li class="color-box">
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

<style scoped>
.color-box {
  background-color: #f7f6f2;
}
#classification {
  width: 200px;
  border: 1px solid #e6e6e6;
  display: inline-flex;
  justify-content: center;
}
#classification ul {
  width: 100%;
  margin: 0;
  padding: 0;
}
#classification li {
  text-align: center;
  list-style: none;
  height: 50px;
  line-height: 50px;
  cursor: pointer;
}
#classification li:hover a {
  color: #ed4259;
}
#classification li a {
  user-select: none;
  color: #2c3e50;
  text-decoration: none;
}
#classification li span {
  margin-right: 10px;
}
</style>
