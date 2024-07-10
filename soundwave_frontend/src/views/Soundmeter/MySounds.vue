<template>
  <div>
      <h1 class="title">My Sounds</h1>
      <div v-if="sounds.length">
          <div class="columns is-multiline">
              <div class="column is-one-third" v-for="sound in sounds" :key="sound.id">
                  <div class="card">
                      <div class="card-content">
                          <p class="title is-4">{{ sound.title }}</p>
                          <p>{{ sound.description }}</p>
                          <p>Duration: {{ sound.duration }} seconds</p>
                          <p>Min dB: {{ sound.min_db_size }}</p>
                          <p>Max dB: {{ sound.max_db_size }}</p>
                          <p>Avg dB: {{ sound.avg_db_size }}</p>
                      </div>
                  </div>
              </div>
          </div>
      </div>
      <div v-else>
          <p>No sounds recorded yet.</p>
      </div>
  </div>
</template>

<script>
export default {
    data() {
        return {sounds: [], 
        };
    },
    created() {
        this.fetchSounds();
    },
    methods: {
    fetchSounds() {
      fetch('http://127.0.0.1:8000/api/v1/sounds/', {
        headers: {
          'Authorization': 'Bearer ' + localStorage.getItem('token') // Ajoute l'authentification si nécessaire
        }
      })
      .then(response => response.json())
      .then(data => {
        this.sounds = data.filter(sound => sound.owner === 8); // Filtre pour obtenir uniquement les sons de l'utilisateur connecté
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
  }
};
</script>
