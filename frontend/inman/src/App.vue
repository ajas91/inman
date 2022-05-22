<template>
  <div class="container-fluid">
    <Header />
    <div class="container-fluid">
      <div class="row mt-2 mb-2 ml-2 mr-2">
        <router-view />
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer'

export default {
  name:'App',
  components: {
    Header,
    Footer,
  },
  data() {
    return {}
  }
}

</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
