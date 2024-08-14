  <template>
    <button @click="toggleTheme" class="button is-primary">
      {{ isDarkTheme ? $t('themeLight') : $t('themeDark') }} 
    </button>
  </template>
  
  <script>
  import { mapState } from 'vuex';
  import { mapMutations } from 'vuex';
  
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
        document.documentElement.className = newTheme;
      }
    },
    created() {
      // Appliquer le thème initial
      document.documentElement.className = this.theme;
    }
  };
  </script>
  