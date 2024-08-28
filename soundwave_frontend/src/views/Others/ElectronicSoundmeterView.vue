<template>
    <div class="electronic" :class="themeClass">
      
      <section class="hero is-medium mb-6" :class="themeClass">
        <div class="hero-body has-text-centered">
          <p class="title mb-6" :class="themeClass">About the Electronic Soundmeter</p>
          <p class="subtitle" :class="themeClass">
            Welcome to the electronic soundmeter documentation page. Here you will find detailed information about the components used, how the device functions, and how to test it using the Soundmeter application.
          </p>
        </div>
      </section>
  
      <section class="hero is-medium mb-6" :class="themeClass">
        <div class="hero-body">
          <div class="columns">
            <div class="column is-half">
              <img src="../../assets/images/electronic.jpg" alt="Electronic Soundmeter Materials" class="image is-4by3">
            </div>
            <div class="column is-half">
              <p class="title" :class="themeClass">Materials Used</p>
              <ul class="content" :class="themeClass">
                <li>Arduino Uno</li>
                <li>Microphone Sensor KY-037</li>
                <li>LEDs (10x)</li>
                <li>Resistors (220Ω)</li>
                <li>Breadboard and Jumper Wires</li>
                <li>USB Cable for Arduino</li>
              </ul>
            </div>
          </div>
        </div>
      </section>
  
      <section class="hero is-medium mb-6" :class="themeClass">
        <div class="hero-body has-text-centered">
          <p class="title" :class="themeClass">How It Works and Testing</p>
          <br>
          <p class="subtitle" :class="themeClass">
            The electronic soundmeter functions by capturing sound through the microphone sensor, converting it into an analog signal, and then processing this signal to estimate the sound level in decibels. The LED indicators provide a visual representation of the sound level, with more LEDs lighting up as the sound level increases.
          </p>
          <p class="subtitle" :class="themeClass">
            To test your soundmeter, connect it to your computer and use our <router-link to="/sound-meter">online Soundmeter</router-link> for calibration and comparison. Make sure your Arduino is properly connected, and watch the LEDs respond to changes in the ambient sound.
          </p>
        </div>
      </section>
  
    </div>
  </template>
  
  <script>
  import { mapState } from 'vuex'
  
  export default {
    name: "ElectronicSoundmeter",
    computed: {
      ...mapState(['theme']),
      themeClass() {
        return this.theme === 'dark' ? 'is-dark' : 'is-light';
      }
    },
    mounted() {
      document.title = this.$t('electronic');
    },
  }
  </script>
