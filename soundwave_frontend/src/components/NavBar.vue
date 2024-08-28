<template>
  <nav :class="['navbar', themeClass]"> 
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item">
        <img src="../assets/mini_logo.png" alt="logo">
        <strong>{{ $t('soundwave') }}</strong>
      </router-link>

      <a
        role="button"
        class="navbar-burger"
        :class="{ 'is-active': isBurgerActive }"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbar-menu"
        @click="toggleBurgerMenu"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div :class="{ 'navbar-menu': true, 'is-active': isBurgerActive }" id="navbar-menu">
      <div class="navbar-end">
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">Menu</a>
          <div class="navbar-dropdown">
            <router-link to="/sound-meter" class="navbar-item"><strong>{{ $t('soundMeter') }}</strong></router-link>
            <router-link to="/sound-map" class="navbar-item"><strong>{{ $t('soundMap') }}</strong></router-link>
            <router-link to="/sound-news" class="navbar-item"><strong>{{ $t('soundNews') }}</strong></router-link>
            <router-link to="/electronic" class="navbar-item"><strong>{{ $t('electronic') }}</strong></router-link>
            <hr class="navbar-divider" />
            <router-link to="/my-sounds" class="navbar-item">{{ $t('mySounds') }}</router-link>
          </div>
        </div>

        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">{{ $t('language') }}</a>
          <div class="navbar-dropdown">
            <a @click="changeLocale('en')" class="navbar-item"><flag iso="gb"/>&nbsp; English</a>
            <a @click="changeLocale('de')" class="navbar-item"><flag iso="de"/>&nbsp; Deutsch</a>
            <a @click="changeLocale('fr')" class="navbar-item"><flag iso="fr"/>&nbsp; Français</a>
            <a @click="changeLocale('nl')" class="navbar-item"><flag iso="nl"/>&nbsp; Nederlands</a>
          </div>
        </div>

        <div class="navbar-item">
          <div class="buttons">
            <ThemeSwitcher />
            <router-link v-if="isAuthenticated" to="/account" class="button" :class="themeClass">
              <strong>{{ $t('accountButton') }}</strong>
            </router-link>
            <router-link v-else to="/log-in" class="button" :class="themeClass">
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
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'NavBar',
  components: {
    ThemeSwitcher
  },
  data() {
    return {
      isBurgerActive: false,
    };
  },
  computed: {
    ...mapState(['isAuthenticated', 'language', 'theme']),
    themeClass() {
      return this.theme === 'dark' ? 'is-dark' : 'is-light';
    }
  },
  methods: {
    ...mapMutations(['setLanguage']),
    changeLocale(locale) {
      this.setLanguage(locale);
    }
  },
  watch: {
    language(newLang) {
      this.$i18n.locale = newLang;

      setTimeout(() => {
        window.location.reload();
      }, 10); 
    }
  },
  created() {
    this.$i18n.locale = this.language;
  }
}
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

body {
  padding-top: 56px;
}

.navbar-burger {
  display: none;
}

@media screen and (max-width: 1023px) {
  .navbar-burger {
    display: block;
  }
}
</style>
