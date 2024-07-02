<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><img src="../src/assets/mini_logo.png" alt="logo"><strong>Soundwave</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-end">
          <router-link to="/" class="navbar-item"><strong>Langage</strong></router-link>
          <router-link to="/" class="navbar-item"><strong>Light/dark mode</strong></router-link>

          <div class="navbar-item">
            <div class="buttons">
              <template v-if="isAuthenticated">
                <span class="navbar-item">La connexion fonctionne</span>
                <button class="button is-light" @click="logOut"><strong>Log out</strong></button>
              </template>
              <template v-else>
                <router-link to="/log-in" class="button is-light"><strong>Log in</strong></router-link>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>
    
    <section class="section">
      <router-view/>
    </section>

    <footer class="footer is-flex-align-items-flex-end mt-auto">
      <p class="has-text-centered">Copyright (c) 2024</p>
      <p class="has-text-centered">
        <router-link to="/about">About  </router-link>
        <router-link to="/privacy">Privacy    </router-link>
        <router-link to="/terms">Terms    </router-link>
        <router-link to="/cookies">Cookies    </router-link>
        <router-link to="/accessibility">Accessibility</router-link>
      </p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  computed: {
    ...mapState(['isAuthenticated', 'user'])
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }

    console.log('User after store initialization:', this.$store.state.user)
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
</style>
