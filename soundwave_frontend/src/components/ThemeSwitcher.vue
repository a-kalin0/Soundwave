<template>
  <button @click="toggleTheme" class="button is-primary">
    {{ isDarkTheme ? 'Switch to Light Mode' : 'Switch to Dark Mode' }}
  </button>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  computed: {
    ...mapState(['theme']),
    isDarkTheme() {
      return this.theme === 'dark';
    }
  },
  methods: {
    ...mapMutations(['setTheme']),
    toggleTheme() {
      const newTheme = this.isDarkTheme ? 'light' : 'dark';
      this.setTheme(newTheme);

      setTimeout(() => {
        window.location.reload();
      }, 10); 
    }
  }
};
</script>
