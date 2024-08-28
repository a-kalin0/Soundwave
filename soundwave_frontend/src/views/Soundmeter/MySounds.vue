<template>
  <div>
    <h1 class="title">My Sounds</h1>
    <button @click="showImportModal()" class="button is-primary">Import Measure From Your Electronic SoundMeter</button>

    <div v-if="sounds.length">
        <div class="columns is-multiline">
            <div class="column is-one-third" v-for="sound in sounds" :key="sound.id">
                <div :class="['card', cardColor(sound.avg_db_size)]">
                    <div class="card-content">
                        <p class="title is-4">{{ sound.title }}</p>
                        <p>{{ sound.description }}</p>
                        <p>Duration: {{ sound.duration }} seconds</p>
                        <p>Min dB: {{ sound.min_db_size }}</p>
                        <p>Max dB: {{ sound.max_db_size }}</p>
                        <p>Avg dB: {{ sound.avg_db_size }}</p>
                        <p>Date Added: {{ new Date(sound.created_at).toLocaleString() }}</p>
                        <div class="buttons">
                          <button @click="showDeleteModal(sound)" class="button is-danger">Delete Record</button>
                          <button @click="showShareModal(sound)" class="button is-link" v-if="!sound.is_shared">Share on the map</button>
                          <button @click="showHideModal(sound)" class="button is-light" v-if="sound.is_shared">Hide from the map</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div v-else>
        <p>No sounds recorded yet.</p>
    </div>

    <!-- Delete Modal -->
    <div class="modal" :class="{'is-active': isDeleteModalActive }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Delete Sound</p>
          <button class="delete" @click="hideDeleteModal" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
          <p>Are you sure you want to delete this sound ?</p>
          <p><strong>{{ selectedSound?.title }}</strong></p>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-danger" @click="deleteSound">Delete</button>
          <button @click="hideDeleteModal">Cancel</button>
        </footer>
      </div>
    </div>

    <!-- Share Modal -->
    <div class="modal" :class="{ 'is-active': isShareModalActive }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Share Sound</p>
          <button class="delete" @click="hideShareModal" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
          <p>Share this sound :
          <strong>{{ selectedSound?.title }}</strong></p>

          <form v-if='!selectedSound?.location' @submit.prevent="shareSound">
            <div class="field">
              <label class="label">Street</label>
              <div class="control">
                <input type="text" class="input" v-model="street" placeholder="Street" required>
              </div>
            </div>
            <div class="field">
              <label class="label">Postcode</label>
              <div class="control">
                <input class="input" type="number" v-model="postcode" placeholder="Postcode" required>
              </div>
            </div>
            <div class="field">
              <label class="label">Place</label>
              <div class="control">
                <input type="text" class="input" v-model="locality" placeholder="Locality" required>
              </div>
            </div>
            <div class="field">
              <label class="label">Country</label>
              <div class="control">
                <input class="input" type="text" v-model="country" placeholder="Country" required>
              </div>
            </div>

            <div class="field is-grouped">
              <div class="control">
                <button class="button is-link" type="submit">Share</button>
              </div>
              <div class="control">
                <button class="button is-light" @click="hideShareModal" type="button">Cancel</button>
              </div>
            </div>
          </form>

          <div v-else>
            <div class="buttons">
              <button class="button is-link" @click="confirmShare">Confirm</button>
              <button class="button is-light" @click="hideShareModal">Cancel</button>
            </div>
          </div>

        </section>
      </div>
    </div>

     <!-- Hide Modal -->
    <div class="modal" :class="{'is-active': isHideModalActive }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Hide Sound</p>
          <button class="delete" @click="hideHideModal" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
          <p>Are you sure you want to hide this sound ?</p>
          <p><strong>{{ selectedSound?.title }}</strong></p>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-danger" @click="hideSound">Hide</button>
          <button @click="hideHideModal">Cancel</button>
        </footer>
      </div>
    </div>

    <!-- Import Modal -->
    <div class="modal" :class="{'is-active': isImportModalActive }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Import Measures</p>
          <button class="delete" @click="closeModal"></button>
        </header>
        <section class="modal-card-body">
          <form @submit.prevent="importMeasure">
            <div class="field">
              <label class="label">Upload JSON File</label>
              <div class="control">
                <input type="file" @change="onFileChange" class="input" accept=".json" required>
              </div>
            </div>
            <div class="field is-grouped">
              <div class="control">
                <button type="submit" class="button is-link">Import</button>
              </div>
              <div class="control">
                <button type="button" class="button is-light" @click="closeModal">Cancel</button>
              </div>
            </div>
          </form>
        </section>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import { getCookie } from '@/utils/cookies-utils.js'

export default {
    data() {
        return {
          sounds: [],
          userId: null, 
          isDeleteModalActive: false,
          isShareModalActive: false,
          isHideModalActive: false,
          isImportModalActive: false,
          selectedSound: null,
          street: '',
          postcode: '',
          locality: '',
          country: '',
          mapboxToken: null,
          selectedFile: null,
        };
    },
    async created() {
      await this.getUserId()
      await this.fetchSounds()
      await this.get_mapbox_api_key()
    },
    mounted() {
      document.title = this.$t('mySounds');
    },
    methods: {
    async getUserId() {
      try {
          const token = getCookie('token');
          const response = await axios.get('/api/v1/users/me/', {
              headers: {
                  'Authorization': 'Token ' + token,
              }
          });
          const user = response.data;
          this.userId = user.id;
      } catch (error) {
          console.error('Error:', error);
      }
    },
    onFileChange(event){
      this.selectedFile = event.target.files[0];
    },
    showImportModal() {
      this.isImportModalActive = true;
    },
    hideImportModal() {
      this.isImportModalActive = false;
      this.selectedFile = null;
    },
    async importMeasure() {
      if (!this.selectedFile) {
        alert('Please select a file to upload.');
        return;
      }

      const formData = new FormData();
      formData.append('file', this.selectedFile);

      try {
        await axios.post('/api/v1/import_measure/', formData, {
          headers: {
            'Authorization': 'Token ' + getCookie('token'),
          },
        })
        this.hideImportModal()
        this.fetchSounds()
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async fetchSounds() {

      try {
        const response = await axios.get('/api/v1/sounds/', {
          headers: {
            'Authorization': 'Token ' + getCookie('token'),
          },
        });
        this.sounds = response.data.filter(sound => sound.owner === this.userId);
      } catch (error) {
        console.error('Error:', error);
      } 
    },
    cardColor(avg){
      if (avg < 70) {
        return 'is-success';
      } else if (avg >= 70 && avg <= 90) {
        return 'is-warning';
      } else {
        return 'is-danger';
      }
    },
    showDeleteModal(sound) {
      this.selectedSound = sound;
      this.isDeleteModalActive = true;
    },
    hideDeleteModal() {
      this.isDeleteModalActive = false;
      this.selectedSound = null;
    },
    async deleteSound() {
      try {
        await axios.delete(`/api/v1/sounds/${this.selectedSound.id}/`, {
          headers: {
            'Authorization': 'Token ' + getCookie('token'),
          },
        });
        this.sounds = this.sounds.filter(sound => sound.id !== this.selectedSound.id);
        this.hideDeleteModal();
          
        toast({
            message: 'Sound deleted successfully',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          });
        } catch (error) {
          console.error('Error:', error);
        }
    },
    showShareModal(sound) {
      this.selectedSound = sound;
      this.isShareModalActive = true;
    },
    hideShareModal() {
      this.isShareModalActive = false;
      this.selectedSound = null;
    },
    async confirmShare() {
      try {
        await axios.patch(`/api/v1/sounds/${this.selectedSound.id}/`, {
          is_shared: true,
        }, {
          headers: {
            'Authorization': 'Token ' + getCookie('token'),
            'Content-Type': 'application/json',
          },
        });
        this.hideShareModal();
        
        toast({
            message: 'Sound shared successfully',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          });

        this.$router.push('/sound-map');
      } catch (error) {
        console.error('Error:', error);
      }
    },

    async get_mapbox_api_key() {
      try {
        const response = await axios.get('/api/v1/get-mapbox-api-key/');
        this.mapboxToken = response.data.mapbox_api_key;
      } catch (error) {
        console.error('Error fetching Mapbox token:', error);
      }
    },
    async shareSound() {

      try {
        const location = `${this.street} ${this.postcode} ${this.locality}, ${this.country}`;

        const mapboxResponse = await axios.get(`https://api.mapbox.com/search/geocode/v6/forward?q=${location}`, {
          params: {
            access_token: this.mapboxToken,
          },
        });

        if (mapboxResponse.data.features && mapboxResponse.data.features.length > 0) {
          const coordinates = mapboxResponse.data.features[0].properties.coordinates;

          
          const [lng, lat] = [coordinates.longitude, coordinates.latitude];
          

          await axios.patch(`/api/v1/sounds/${this.selectedSound.id}/`, {
            location: location,
            latitude: lat,
            longitude: lng,
            is_shared: true,
          }, {
            headers: {
              'Authorization': 'Token ' + getCookie('token'),
              'Content-Type': 'application/json',
            },
          
          });

          this.hideShareModal();

          toast({
            message: 'Sound shared successfully',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 2000,
            position: 'bottom-right',
          })

             this.$router.push('/sound-map');
          } else {
              console.error('Problem with location');
          }
        } catch(error) {
          console.error('Error:', error);
        }
    },
    showHideModal(sound) {
      this.selectedSound = sound;
      this.isHideModalActive = true;
    },
    hideHideModal() {
      this.isHideModalActive = false;
      this.selectedSound = null;
    },
    async hideSound() {
      try {
        await axios.patch(`/api/v1/sounds/${this.selectedSound.id}/`, {
          is_shared: false,
        }, {
          headers: {
            'Authorization': 'Token ' + getCookie('token'),
            'Content-Type': 'application/json',
          },
        });

        this.sounds = this.sounds.map(sound => {
          if (sound.id === this.selectedSound.id) {
            return { ...sound, is_shared: false };
          }
          return sound;
        });
        this.hideHideModal();

        toast({
          message: 'Sound hidden successfully',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right',
        });
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>

<style scoped>
.card.is-success {
  border-left: 5px solid green /* Vert clair */
}
.card.is-warning {
  border-left: 5px solid yellow; /* Jaune clair */
}
.card.is-danger {
  border-left: 5px solid red; /* Rouge clair */
}
.card {
  margin: 1rem;
}
</style>