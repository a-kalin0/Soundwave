<template>
    <div class="map-wrap">
      <a href="https://www.maptiler.com" class="watermark"><img
          src="https://api.maptiler.com/resources/logo.svg" alt="MapTiler logo"/></a>
      <div class="map" ref="mapContainer"></div>
    </div>
  </template>
  
  <script>
  import maplibregl from 'maplibre-gl';
  import { Map, Marker } from 'maplibre-gl';
  import { shallowRef, onMounted, onUnmounted, markRaw } from 'vue';
  
  export default {
    name: "MapSound",
    setup () {
      const mapContainer = shallowRef(null);
      const map = shallowRef(null);
  
      onMounted(() => {
        fetch('http://127.0.0.1:8000/api/v1/get-maptiler-api-key/')
         .then(response => response.json()
         )
         .then(data => {
          const apiKey = data.maptiler_api_key;

          const initialState = { lng: 4.3528, lat: 50.8466, zoom: 7 };
  
          map.value = markRaw(new Map({
            container: mapContainer.value,
            style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${apiKey}`,
            center: [initialState.lng, initialState.lat],
            zoom: initialState.zoom
          }));

        fetch('http://127.0.0.1:8000/api/v1/sounds/', {
          headers: {
            'Authorization': 'Token' + localStorage.getItem('token'),
          }
        })
        .then(response => response.json())
        .then(data => {
          data.forEach(sound => {
            if (sound.is_shared && sound.latitude && sound.longitude) {

              const popupContent = `
                <div>
                  <h3>${sound.title}</h3>
                  <p>${sound.description}</p>
                  <p>Min dB: ${sound.min_db_size}</p>
                  <p>Max dB: ${sound.max_db_size}</p>
                  <p>Avg dB: ${sound.avg_db_size}</p>
                  <p>Date: ${new Date(sound.created_at).toLocaleString()}</p>
                </div>`;

              const popup = new maplibregl.Popup().setHTML(popupContent)

              new Marker({ color: getMarkerColor(sound.avg_db_size) })
              .setLngLat([sound.longitude, sound.latitude])
              .setPopup(popup)
              .addTo(map.value);
            }
          });
        })
        .catch((error) => {
          console.error('Error:', error);
        });

        });
  
      }),
      onUnmounted(() => {
        map.value?.remove();
      })

      const getMarkerColor = (avgDb) => {
        if (avgDb < 70) {
          return 'green';
        } else if (avgDb >= 70 && avgDb <= 90) {
          return 'yellow';
        } else {
          return 'red';
        }
      };
      
      return {
        map, mapContainer
      };
    }
  };
  </script>
  
  
  <style scoped>
  @import '~maplibre-gl/dist/maplibre-gl.css';
  
  .map-wrap {
    position: relative;
    width: 100%;
    height: calc(100vh - 77px); 
  }
  
  .map {
    position: absolute;
    width: 100%;
    height: 100%;
  }
  
  .watermark {
    position: absolute;
    left: 10px;
    bottom: 10px;
    z-index: 999;
  }
  </style>