<template>
    <div>
        <h1>My Sounds</h1>
        <div v-if="sounds.length">
            <ul>
                <li v-for="sound in sounds" :key="sound.id">
                    <h2>{{ sound.title }}</h2>
                    <p>{{ sound.description }}</p>
                    <p>Duration : {{ sound.duration }}</p>
                    <p>Min dB : {{ sound.min_db_size }}</p>
                    <p>Max dB : {{ 
                    sound.max_db_size }}</p>
                    <p>Avg dB : {{ sound.avg_db_size }}</p>
                </li>
            </ul>
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

<style scoped>
h1 {
  margin-bottom: 1rem;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1rem;
}
</style>