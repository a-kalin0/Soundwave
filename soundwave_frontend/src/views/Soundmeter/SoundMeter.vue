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

    <div class="columns">
      <div class="column">
        <p class="decibels is-dark">Current Decibel Level : {{ decibels.toFixed(2) }} dB</p>
        <div class="controls">
          <button @click="startRecording" v-if="!recording && !stopped">Start Recording</button>
          <button @click="stopRecording" v-if="recording">Stop Recording</button>
          <button @click="showModal" v-if="stopped">Save Record</button>
          <button @click="resetRecord" v-if="stopped">Make Another Record</button>
        </div>
      </div>
      <div class="column">
        <div class="timer">
          <p>Recording time : {{ formattedTime }}</p>
        </div>
        <div class="stats">
          <div class="stat">
            <span>MIN : </span>
            <span>{{ min.toFixed(2) }} dB</span>
          </div>
          <div class="stat">
            <span>MAX : </span>
            <span>{{ max.toFixed(2) }} dB</span>
          </div>
          <div class="stat">
            <span>AVG : </span>
            <span>{{ average.toFixed(2) }} dB</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Save Record Modal -->
    <div class="modal" :class="{ 'is-active': isModalActive }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Save Record</p>
          <button class="delete" @click="hideModal" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
          <form @submit.prevent="saveRecord">
            <div class="field">
              <label class="label">Title</label>
              <div class="control">
                <input type="text" class="input" v-model="title" required>
              </div>
            </div>
            <div class="field">
              <label class="label">Description</label>
              <div class="control">
                <textarea class="textarea" v-model="description" required></textarea>
              </div>
            </div>
            <div class="field">
              <label class="label">Average dB</label>
              <div class="control">
                <input type="text" class="input" :value="Math.round(average)" readonly>
              </div>
            </div>
            <div class="field">
              <label class="label">Min dB</label>
              <div class="control">
                <input type="text" class="input" :value="Math.round(min)" readonly>
              </div>
            </div>
            <div class="field">
              <label class="label">Max dB</label>
              <div class="control">
                <input type="text" class="input" :value="Math.round(max)" readonly>
              </div>
            </div>
            <div class="field is-grouped">
              <div class="control">
                <button class="button is-link" type="submit">Save</button>
              </div>
              <div class="control">
                <button class="button is-light" @click="hideModal" type="button">Cancel</button>
              </div>
            </div>
          </form>
        </section>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
import { toast } from 'bulma-toast';
  
export default {
    name: 'SoundMeter',
    data() {
      return {
        decibels: 0,
        min : Infinity,
        max : -Infinity,
        average: 0,
        time : 0,
        recording: false,
        stopped: false,
        timerInterval: null,

        audioContext: null,
        mediaStreamSource: null,
        workletNode: null,
        sampleCount: 0,
        totalDb: 0,

        isModalActive: false,
        title: '',
        description: '',
        userId: null,
      };
    },
    computed: {
      formattedTime() {
        const minutes = Math.floor(this.time / 60);
        const seconds = this.time % 60;
        return `${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
      },
    },
    methods: {
      async startRecording() {
        this.recording = true;
        this.stopped = false;
        this.startTimer();

        this.audioContext = new (window.AudioContext)();

        const processorCode = `
          class AudioProcessor extends AudioWorkletProcessor {
            constructor() {
              super();
              this._lastUpdateTime = 0;
            }

            process(inputs, outputs, parameters) {
              const input = inputs[0];
              if (input.length > 0) {
                const channelData = input[0];
                let sum = 0;
                for (let i = 0; i < channelData.length; i++) {
                  sum += channelData[i] * channelData[i];
                }
                const rms = Math.sqrt(sum / channelData.length);
                let db = 20 * Math.log10(rms) + 100;

                const currentTime = currentFrame / sampleRate;
                if (currentTime - this._lastUpdateTime >= 0.2) {
                  this.port.postMessage(db);
                  this._lastUpdateTime = currentTime;
                }
              }
              return true;
            }
          }

          registerProcessor('audio-processor', AudioProcessor);
      `;

      const blob = new Blob([processorCode], { type: 'application/javascript' });
      const url = URL.createObjectURL(blob);

      try {
        await this.audioContext.audioWorklet.addModule(url);
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        this.mediaStreamSource = this.audioContext.createMediaStreamSource(stream);
        this.workletNode = new AudioWorkletNode(this.audioContext, 'audio-processor');

        this.workletNode.port.onmessage = (event) => {
          const db = event.data;
          this.decibels = db;
          this.updateStats(db);
        }
        
        this.mediaStreamSource.connect(this.workletNode);
        this.workletNode.connect(this.audioContext.destination);
      } catch (err) {
        console.error('Error accessing microphone', err);
      }
    },
      stopRecording() {
        this.recording = false;
        this.stopped = true;
        this.stopTimer();

        if (this.measureInterval) {
          clearInterval(this.measureInterval);
          this.measureInterval = null;
        }
        if (this.workletNode) {
          this.workletNode.disconnect();
        }
        if (this.mediaStreamSource) {
          this.mediaStreamSource.disconnect();
        }
        if (this.audioContext) {
          this.audioContext.close();
        }
      },
      showModal() {
        this.isModalActive = true;
      },
      hideModal() {
        this.isModalActive = false;
      },
      async saveRecord() {
        const userId = await this.getUserId();
        const recordData = {
          'title': this.title,
          'description': this.description,
          'duration': this.time,
          'min_db_size': Math.round(this.min),
          'max_db_size': Math.round(this.max),
          'avg_db_size': Math.round(this.average),
          'owner': userId
        };

        fetch('http://127.0.0.1:8000/api/v1/sounds/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(recordData)
          
        })
         .then(response => response.json())
         .then(          
          toast({
            message: 'Sound created successfully',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          }))
         .then(this.$router.push('/my-sounds'))
         .catch((error) => {
          console.error('Error:', error);
         });
      },
      async getUserId(){
        try {
          const response = await axios.get('/api/v1/users/me/')
          const user = response.data

          return user.id;
        } catch (error) {
          console.error('Error:', error);
        }
      },
      resetRecord() {
        this.stopped = false;
        this.resetStats();
        this.startRecording();
      },
      startTimer() {
        this.timerInterval = setInterval(() => {
          this.time++;
        }, 1000);
      },
      stopTimer() {
        clearInterval(this.timerInterval);
        this.timerInterval = null;
      },
      updateStats(db){
        if (db < this.min) {
          this.min = db;
        }
        if (db > this.max) {
          this.max = db;
        }
        this.sampleCount++;
        this.totalDb += db;
        this.average = this.totalDb / this.sampleCount;
      },
      resetStats() {
        this.time = 0;
        this.decibels = 0;
        this.min = Infinity;
        this.max = -Infinity;
        this.average = 0;
        this.sampleCount = 0;
        this.totalDb = 0;
      }
    },
  }
</script>
  

<style scoped>
.home {
  text-align: center;
}
.hero {
  margin-bottom: 2rem;
}
.columns {
  display: flex;
  justify-content: center;
}
.column {
  flex: 1;
  padding: 1rem;
}
.decibels {
  font-size: 2rem;
  margin-bottom: 1rem;
}
.controls button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  margin: 0 10px;
}
.timer {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}
.stats {
  margin-top: 1rem;
}
.stat {
  margin: 0.5rem 0;
}
.modal-card {
  width: 90%;
  max-width: 640px;
}
</style>