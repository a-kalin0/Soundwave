<template>
    <div class="terms" :class="themeClass">

    <section class="hero is-medium mb-6" :class="themeClass">
        <div class="hero-body has-text-centered">
            <p class="title mb-6" :class="themeClass">Terms of Service</p>
            <p class="subtitle" :class="themeClass">
            Ici vous trouverez les informations sur la façon dont les données des utilisateurs sont utilisées.
            </p>
        </div>
    </section>

    <section class="hero is-medium mb-6" :class="themeClass">
        <div class="hero-body has-text-centered">
            <p class="title mb-6" :class="themeClass">Cookies et Comptes</p>
            <p class="subtitle" :class="themeClass">
            Notre site utilise des cookies pour gérer les sessions utilisateur, mémoriser les préférences (comme le thème), et sécuriser les connexions. Les comptes utilisateurs permettent de sauvegarder vos mesures et de personnaliser votre expérience sur Soundwave.
            </p>
        </div>
    </section>

    <section class="hero is-medium mb-6" :class="themeClass">
        <div class="hero-body has-text-centered">
            <p class="title mb-6" :class="themeClass">Sonometre</p>
            <p class="subtitle" :class="themeClass">
            Le sonomètre utilise l'API Web Audio pour capturer et analyser les sons environnants. Les "sons" enregistrés ne sont pas réellement des fichiers audio mais des mesures de valeurs en décibels, qui sont stockées pour l'analyse statistique et l'amélioration du service.
            </p>
        </div>
    </section>

    <section class="hero is-medium mb-6" :class="themeClass">
        <div class="hero-body has-text-centered">
            <p class="title mb-6" :class="themeClass">Soundmap</p>
            <p class="subtitle" :class="themeClass">
            La Soundmap utilise plusieurs APIs pour afficher et partager les niveaux sonores enregistrés par les utilisateurs. Cela inclut les APIs de géolocalisation pour positionner les mesures sur une carte interactive.
            </p>
        </div>
    </section>

    </div>
</template>

  <script>
  import { mapState } from 'vuex';
  
  export default {
    name: "TermsView",
    computed: {
      ...mapState(['theme']),
      themeClass() {
        return this.theme === 'dark' ? 'is-dark' : 'is-light';
      }
    },
    mounted() {
      document.title = 'Terms of Service';
    }
  }
  </script>
  
  <style scoped>
  
  .hero {
    padding: 3rem 1.5rem;
    margin-bottom: 2rem;
  }
  
  </style>
  