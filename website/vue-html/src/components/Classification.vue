<template>
  <div id="classification">
    <ul>
      <li>
        <router-link to="#">
          <span class="iconfont icon-xuanhuan"></span>
          玄幻魔法
        </router-link>
      </li>
      <li>
        <router-link to="#">
          <span class="iconfont icon-wuxia"></span>武侠修真
        </router-link>
      </li>
      <li>
        <router-link to="#">
          <span class="iconfont icon-dushi"></span>都市言情
        </router-link>
      </li>
      <li>
        <router-link to="#">
          <span class="iconfont icon-junshi"></span>历史军事
        </router-link>
      </li>
      <li>
        <router-link to="#">
          <span class="iconfont icon-erciyuan"></span>网游动漫
        </router-link>
      </li>
      <li>
        <router-link to="#">
          <span class="iconfont icon-kehuan"></span>科幻小说
        </router-link>
      </li>
      <li>
        <router-link to="#">
          <span class="iconfont icon-lingyi"></span>恐怖灵异
        </router-link>
      </li>
      <li>
        <router-link to="#">
          <span class="iconfont icon-other"></span>其他小说
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
#classification {
  background-color: rgba(30, 35, 38, 0.8);
  width: 200px;
  padding: 20px 0;
  display: inline-flex;
  justify-content: center;
  border-radius: 20px;
}
#classification ul {
  margin: 0;
  padding: 0;
}
#classification li {
  list-style: none;
  height: 50px;
  line-height: 50px;
}
#classification li a{
    color: rgb(217, 217, 217);
    text-decoration: none;
}
#classification li span {
  margin-right: 10px;
}
</style>
