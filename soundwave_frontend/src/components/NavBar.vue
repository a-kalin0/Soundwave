<template>
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <img src="../assets/mini_logo.png" alt="logo">
        <strong>Soundwave</strong>
      </router-link>

      <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div class="navbar-menu" id="navbar-menu">
      <div class="navbar-end">
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            Menu
          </a>
          <div class="navbar-dropdown">
            <router-link to="/sound-meter" class="navbar-item"><strong>Soundmeter</strong></router-link>
            <router-link to="/sound-map" class="navbar-item"><strong>Soundmap</strong></router-link>
            <router-link to="/sound-news" class="navbar-item"><strong>Soundnews</strong></router-link>
            <router-link to="/" class="navbar-item"><strong>Light/dark mode</strong></router-link>
            <hr class="navbar-divider" />
            <router-link to="/" class="navbar-item">More</router-link>
          </div>
        </div>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            {{ $t('language') }}
          </a>
          <div class="navbar-dropdown">
            <a @click="changeLocale('en')" class="navbar-item"> <flag iso="gb"/> | English</a>
            <a @click="changeLocale('fr')" class="navbar-item"> <flag iso="fr"/> | Français</a>
            <a @click="changeLocale('nl')" class="navbar-item"> <flag iso="nl"/> | Nederlands</a>
            <a @click="changeLocale('de')" class="navbar-item"> <flag iso="de"/> | Deutsch</a>
          </div>
        </div>

        <ThemeSwitcher />

        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/log-in" class="button is-light"><strong>Log in</strong></router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import ThemeSwitcher from './ThemeSwitcher.vue';

export default {
  name: 'NavBar',
  components: {
    ThemeSwitcher
  },
  methods: {
    changeLocale(locale) {
      this.$i18n.locale = locale;
    }
  }
}
</script>

<style scoped>
.fi.fis {
  margin-right: 10px;
}
</style>
