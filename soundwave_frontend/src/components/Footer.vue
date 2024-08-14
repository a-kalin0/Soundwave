<template>
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
</template>

<script>
export default {
  name: 'FooterBar'
}
</script>