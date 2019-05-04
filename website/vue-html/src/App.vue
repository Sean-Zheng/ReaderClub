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
        document.getElementById('navigation').style.backgroundColor='rgba(189, 195, 199,1.0)';
        document.body.style.backgroundColor = "#343f45";
        document.body.style.backgroundImage = '';
      } else {
        document.getElementById('navigation').style.backgroundColor='rgba(189, 195, 199,1.0)';
        document.body.style.backgroundColor = "#ffffff";
        document.body.style.backgroundImage = '';
      }
    }
  }
};
</script>


<style>
body {
  margin: 0;
  background-repeat: repeat;
}
#view {
  padding: 10px 150px;
}
</style>
