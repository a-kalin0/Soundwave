<template>
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <img src="../assets/mini_logo.png" alt="logo">
        <strong>{{ $t('soundwave') }}</strong>
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
            <router-link to="/sound-meter" class="navbar-item"><strong>{{ $t('soundMeter') }}</strong></router-link>
            <router-link to="/sound-map" class="navbar-item"><strong>{{ $t('soundMap') }}</strong></router-link>
            <router-link to="/sound-news" class="navbar-item"><strong>{{ $t('soundNews') }}</strong></router-link>
            <hr class="navbar-divider" />
            <router-link to="/" class="navbar-item">{{ $t('more') }}</router-link>
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

        <div class="navbar-item">
          <div class="buttons">
            <ThemeSwitcher />
            <router-link v-if="isAuthenticated" to="/account" class="button is-light">
              <strong>{{ $t('accountButton') }}</strong>
            </router-link>
            <router-link v-else to="/log-in" class="button is-light">
              <strong>{{ $t('loginButton') }}</strong>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import ThemeSwitcher from './ThemeSwitcher.vue';
import { mapState } from 'vuex';

export default {
  name: 'NavBar',
  components: {
    ThemeSwitcher
  },
  computed: {
    ...mapState(['isAuthenticated'])
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
