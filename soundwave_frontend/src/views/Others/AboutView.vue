<template>
    <div class="about" :class="themeClass">
      <section class="hero is-medium mb-6" :class="themeClass">
        <div class="hero-body has-text-centered">
          <p class="title mb-6" :class="themeClass">
            About me
          </p>
          <p class="subtitle" :class="themeClass">
            Here's the link to my portfolio : <a href="https://a-kalin0.github.io" :class="themeClass">Click Here</a> !
          </p>
        </div>
      </section>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'AboutView',
  computed: {
    ...mapState(['theme']),
    themeClass() {
      return this.theme === 'dark' ? 'is-dark' : 'is-light'
    }
  },
  mounted() {
    document.title = 'About Me';
  }
}
</script>
