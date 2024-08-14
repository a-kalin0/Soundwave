<template>
  <div id="wrapper">

    <NavBar />
    
    <section class="section">
      <router-view/>
    </section>

    <FooterBar />

  </div>
</template>

<script>
import axios from 'axios'
import NavBar from './components/NavBar.vue'
import FooterBar from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    FooterBar,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
@import './assets/styles/styles.scss';
</style>
