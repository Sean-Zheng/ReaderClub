<template>
  <div id="app">
        <Navigation></Navigation>
        <dir id="view">
          <router-view />
        </dir>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
export default {
  components: {
    Navigation
  }
}
</script>


<style>
body{
  background: rgb(49, 60, 64);
  margin: 0; 
}
</style>
