<template>
  <div id="app" ref="main">
    <Navigation></Navigation>
    <dir id="view">
      <router-view/>
    </dir>
  </div>
</template>

<script>
import Navigation from "./components/Navigation";
export default {
  components: {
    Navigation
  },
  watch: {
    $route(to, from) {
      if (to.path === "/login" || to.path === "/register") {
        document.body.style.backgroundColor = "#343f45";
      } else {
        document.body.style.backgroundColor = "#ffffff";
      }
    }
  }
};
</script>


<style>
body {
  margin: 0;
}
#view {
  padding: 10px 150px;
}
</style>
