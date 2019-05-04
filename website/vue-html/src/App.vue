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
  /* background: #f7f6f2; */
  margin: 0; 
}
#view{
  padding: 10px 150px;
}
</style>
