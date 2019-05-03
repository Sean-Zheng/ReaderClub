<template>
  <div id="classification">
    <ul>
      <li><span class="iconfont icon-xuanhuan"></span>玄幻魔法</li>
      <li><span class="iconfont icon-wuxia"></span>武侠修真</li>
      <li><span class="iconfont icon-dushi"></span>都市言情</li>
      <li><span class="iconfont icon-junshi"></span>历史军事</li>
      <li><span class="iconfont icon-erciyuan"></span>网游动漫</li>
      <li><span class="iconfont icon-kehuan"></span>科幻小说</li>
      <li><span class="iconfont icon-lingyi"></span>恐怖灵异</li>
      <li><span class="iconfont icon-other"></span>其他小说</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      key: "value"
    };
  },
  methods: {
    name() {}
  }
};
</script>

<style scoped>
#classification{
  background-color: rgba(30,35,38,0.8);
  width: 200px;
  padding: 20px 0;
  display: flex;
  justify-content: center;
  border-radius: 20px;
}
#classification ul {
  margin: 0;
  padding: 0;
}
#classification li {
  list-style: none;
  height:50px;
  line-height: 50px;
  color: rgb(217, 217, 217);
}
#classification li span{
  margin-right: 10px;
}
</style>
