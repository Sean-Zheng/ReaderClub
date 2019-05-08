<template>
  <div class="comment-item">
    <p>{{Item.comment_text}}</p>
    <div class="box">
      <div class="score-box">
        <el-rate
          v-model="Item.comment_score"
          disabled
          show-score
          text-color="#ff9900"
          score-template="{value}"
        ></el-rate>
      </div>
      <p class="name-box">{{Item.user_name}}</p>
      <p class="time-box">{{Item.comment_time}}</p>
      <p style="clear:both;"></p>
    </div>
  </div>
</template>

<script>
export default {
  name: "comment-item",
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
.comment-item {
  border-bottom: 1px solid #e5e5e5;
  padding: 0 20px 10px;
}
.box {
  margin: 30px 10px;
}
.score-box {
  width: 200px;
  float: left;
}
.time-box {
  width: 200px;
  float: right;
  margin: 0 10px;
}
.name-box {
  width: 200px;
  float: right;
  margin: 0 10px;
}
</style>