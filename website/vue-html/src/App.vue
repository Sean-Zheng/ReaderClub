<template>
  <div id="app" ref="main" @contextmenu.prevent :class="getBodyStyle()">
    <Navigation></Navigation>
    <div id="view">
      <router-view/>
    </div>
  </div>
</template>

<script>
import Navigation from "./components/Navigation";
export default {
  components: {
    Navigation
  },
  methods: {
    getBodyStyle() {
      switch (this.$route.path) {
        case "/":
          return "home-body";
        case "/login":
        case "/register":
          return "user-body";
        case "/chapter":
          return `${this.$store.getters.getTheme}-body`;
        default:
          return "home-body";
      }
    }
  }
};
</script>


<style>
html {
  height: 100%;
}
body {
  margin: 0;
  height: 100%;
  background-repeat: repeat;
}
#app {
  height: 100%;
  overflow: auto;
}
#view {
  /* padding: 0 150px; */
}
.home-body {
  background-color: #ffffff;
}
.user-body {
  background-color: #343f45;
}
.default-body {
  background-image: url("./assets/body0.png");
}
.yellow-body {
  background-image: url("./assets/body1.png");
}
.green-body {
  background-image: url("./assets/body2.png");
}
.blue-body {
  background-image: url("./assets/body3.png");
}
.gray-body {
  background-image: url("./assets/body4.png");
}
.black-body {
  background-image: url("./assets/body5.png");
}
</style>
