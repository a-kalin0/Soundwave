<template>
  <div class="home">

    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to the Soundmeter page !
            </p>
            <p class="subtitle">
                Here you can measure the sound with the online soundmeter ! Enjoy !
                
                <br>
                
                P.S. : Take attention to the fact that it can be less precise than the electronic soundmeter 

            </p>
        </div>
    </section>

    <div class="sound-meter">
      
      <div class="display">
        <h1>Sound Meter</h1>
        <div class="decibels">Current Sound Level : </div>
      </div>

      <div class="stats">
        <div class="stat">
          <span>AVG</span>
          <span></span>
        </div>

        <div class="stat">
          <span>MAX</span>
          <span></span>
        </div>

        <div class="stat">
          <span>MIN</span>
          <span></span>
        </div>

        <div class="controls">
          
        </div>
      </div>

      <button @click="startRecording" v-if="!recording">Start Recording</button>
      <button @click="stopRecording" v-if="recording">Stop Recording</button>
    </div>

  </div>
</template>
  
<script>
  
export default {
    name: 'SoundMeter',
    data() {
      return {
        decibels: 0,
        recording: false,
        audioContext: null,
        meter: null,
      };
    },
    methods: {
      async startRecording() {
        this.recording = true;
        console.log('Recording started')
      },
      stopRecording() {
        this.recording = false;
        console.log('Recording stopped')
      },

    },
    components: {
    }
  }
</script>
  