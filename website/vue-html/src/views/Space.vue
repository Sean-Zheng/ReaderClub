<template>
  <div class="space">
    <personal-message/>
    <div class="blist">
      <shelf-item v-for="item in list" :key="item.source_url" :item="item"></shelf-item>
    </div>
  </div>
</template>

<script>
import PersonalMessage from "@/components/PersonalMessage";
import ShelfItem from "@/components/ShelfItem";
export default {
  name: "space",
  computed: {
    list() {
      return this.$store.getters.getBookList;
    }
  },
  components: {
    PersonalMessage,
    ShelfItem
  },
  created() {
    this.$store.dispatch("getBookListAction");
  }
};
</script>

<style scoped>
.blist {
  margin: 30px auto;
  width: 1080px;
}
</style>