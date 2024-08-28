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
import { mapState } from 'vuex';

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
  computed: {
    ...mapState(['theme']),
  },
  watch: {
    theme(newTheme) {
      this.applyTheme(newTheme);
    }
  },
  mounted() {
    this.applyTheme(this.theme || 'light'); 
  },
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    },
    applyTheme(theme) {
      if (theme === 'dark') {
        require('@/assets/themes/dark-theme.scss');
      } else {
        require('@/assets/themes/light-theme.scss');
      }
      document.body.className = theme; 
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

</style>
