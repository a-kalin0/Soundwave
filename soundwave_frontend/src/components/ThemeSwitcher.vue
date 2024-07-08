<!-- src/components/ThemeSwitcher.vue -->
<template>
    <button @click="toggleTheme" class="button is-primary">
      {{ isDarkTheme ? $t('themeLight') : $t('themeDark') }} 
    </button>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isDarkTheme: false
      };
    },
    computed: {
      themeClass() {
        return this.isDarkTheme ? 'dark-theme' : 'light-theme';
      }
    },
    methods: {
      toggleTheme() {
        this.isDarkTheme = !this.isDarkTheme;
        document.documentElement.className = this.themeClass;
      }
    },
    created() {
      // Apply the initial theme based on isDarkTheme
      document.documentElement.className = this.themeClass;
    }
  };
  </script>
  
  <style scoped>
  
  </style>
  