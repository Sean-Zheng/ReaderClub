<template>
  <div id="bookinfo" v-bind:style="{height:imageHeight}">
    <div v-bind:style="{width:imageWidth}">
      <div id="msg">
        <div>
            <img v-bind:src="image_url" alt="封面加载失败">
        </div>
        <div>
          <h1>{{name}}</h1>
          <h3>作者:{{author}}</h3>
          <p>类型:{{book_type}}</p>
          <p>最近更新:{{update_time}}</p>
          <p>最新章节:{{latest_chapters}}</p>
        </div>
      </div>
      <p>{{description}}</p>
    </div>
  </div>
</template>



<script>
export default {
  //http://flyosity.com/digitalpost/
  name: "BookInfo",
  data() {
    return {
      image_url:
        "https://www.biquge.com.cn/files/article/image/30/30458/30458s.jpg",
      source_url: "https://www.biquge.com.cn/book/30458/",
      name: "大道朝天",
      description:
        "我就是剑。　　千里杀一人，十步不愿行。　　千里杀一人，十步不得行。　　千里杀一人，十步？不行！　　我就是剑，剑就是我。　　大道朝天，各执一剑。　　（欢迎加入猫腻大道朝天官方群，群号码：31187551...",
      author: "猫腻",
      book_type: "玄幻小说",
      update_time: "2019-04-18",
      latest_chapters: "第二十七章青山起微澜"
    };
  },
  computed: {
    imageHeight() {
      return `${document.documentElement.clientHeight * 0.65}px`;
    },

    imageWidth() {
      return `${document.documentElement.clientHeight * 0.45}px`;
    }
  }
};
</script>

<style scoped>
#bookinfo {
  background-image: url("../assets/pages.jpg");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  padding: 30px;
  display: flex;
  justify-content: center;
}
#bookinfo>div {
  display: inline-block;
}
#bookinfo>div>p{
    width: 70%;
    margin: 0 auto;
}
#msg{
    padding: 10% 10%;
}
/* #msg>img {
    float: left;
} */
#msg>div{
    float: right;
}
</style>
