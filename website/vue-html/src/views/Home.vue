<template>
  <div id="home">
    <Classification></Classification>
    <div>
      <Recommend></Recommend>
    </div>
  </div>
</template>

<script>
import Classification from "@/components/Classification";
import Recommend from "@/components/Recommend";
export default {
  name: "home",
  components: {
    Classification,
    Recommend
  },
  created() {
    this.$store.dispatch("homeAction").then(result => {
      if (result !== "ok") {
        this.$message({
          message: "网络错误",
          type: "warning"
        });
      }
    });
  }
};
</script>

<style scoped>
#home {
  display: flex;
  justify-content: space-around;
}
</style>
