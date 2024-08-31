<template>
  <div class="home" :class="themeClass">

    <section class="hero is-medium mb-6" :class="themeClass">
      <div class="hero-body has-text-centered">
        <p class="title mb-6" :class="themeClass">{{ $t('welcomeTitle') }}</p>
        <p class="subtitle" :class="themeClass">{{ $t('welcomeSubtitle') }}</p>
      </div>
    </section>

    <section class="hero is-medium mb-6" :class="themeClass">
      <div class="hero-body has-text-centered">
        <img src="../../assets/logo.png" alt="logo" class="logo-img">
        <p class="subtitle mt-4" :class="themeClass">
           {{ $t('homeContent') }}
        </p>
      </div>
    </section>

    <div class="container">
      <div class="columns is-multiline">

        <!-- Card 1 -->
        <div class="column is-full-mobile is-half-tablet is-one-quarter-desktop">
          <div :class="['card', themeClass]">
            <div class="card-image">
              <router-link to="/sound-meter">
                <figure class="image is-4by3">
                  <img src="../../assets/images/Soundmeter.jpg" alt="Measure sounds placeholder">
                </figure>
              </router-link>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <p class="title is-4" :class="themeClass">{{ $t('soundMeter') }}</p>
                  <br>
                  <p class="subtitle is-6" :class="themeClass">{{ $t('soundmeterSub') }}</p>
                </div>
              </div>
              <div class="content" :class="themeClass">
                 {{ $t('soundmeterContent') }}
              </div>
            </div>
          </div>
        </div>

        <!-- Card 2 -->
        <div class="column is-full-mobile is-half-tablet is-one-quarter-desktop">
          <div :class="['card', themeClass]">
            <div class="card-image">
              <router-link to="/sound-map">
                <figure class="image is-4by3">
                  <img src="../../assets/images/Soundmap.png" alt="Sound map placeholder">
                </figure>
              </router-link>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <p class="title is-4" :class="themeClass">{{ $t('soundMap') }}</p>
                  <br>
                  <p class="subtitle is-6" :class="themeClass">{{ $t('soundmapSub') }}</p>
                </div>
              </div>
              <div class="content" :class="themeClass">
                {{ $t('soundmapContent') }}
              </div>
            </div>
          </div>
        </div>

        <!-- Card 3 -->
        <div class="column is-full-mobile is-half-tablet is-one-quarter-desktop">
          <div :class="['card', themeClass]">
            <div class="card-image">
              <router-link to="/sound-news">
                <figure class="image is-4by3">
                  <img src="../../assets/images/Soundnews.jpg" alt="Sound news placeholder">
                </figure>
              </router-link>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <p class="title is-4" :class="themeClass">{{ $t('soundNews') }}</p>
                  <br>
                  <p class="subtitle is-6" :class="themeClass">{{ $t('soundnewsSub') }}</p>
                </div>
              </div>
              <div class="content" :class="themeClass">
                {{ $t('soundnewsContent') }}
              </div>
            </div>
          </div>
        </div>

        <!-- Card 4 -->
        <div class="column is-full-mobile is-half-tablet is-one-quarter-desktop">
          <div :class="['card', themeClass]">
            <div class="card-image">
              <router-link to="/electronic">
                <figure class="image is-4by3">
                  <img src="../../assets/images/electronic.jpg" alt="Electronic soundmeter placeholder">
                </figure>
              </router-link>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <p class="title is-4" :class="themeClass">{{ $t('electronic') }}</p>
                  <br>
                  <p class="subtitle is-6" :class="themeClass">{{ $t('electronicSub') }}</p>
                </div>
              </div>
              <div class="content" :class="themeClass">
                {{ $t('electronicContent') }}
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'HomeView',
  computed: {
    ...mapState(['theme']),
    themeClass() {
      return this.theme === 'dark' ? 'is-dark' : 'is-light'
    }
  },
  mounted() {
    document.title = this.$t('welcomeTitle')
  }
}
</script>

<style scoped>

.title.is-light, .subtitle.is-light {
  color: #000;
}

.title.is-dark, .subtitle.is-dark {
  color: #fff;
}

.card.is-light {
  background-color: #f2f2f2;
}

.card.is-dark {
  background-color: #444444;
}

.container {
  padding: 20px;
}

.card {
  height: 600px;
}

</style>
