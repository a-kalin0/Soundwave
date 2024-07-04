<template>

<div class="home">

<section class="hero is-medium is-dark mb-6">
    <div class="hero-body has-text-centered">
        <p class="title mb-6">
            Welcome to the Sound Map page !
        </p>
        <p class="subtitle">
            Here you can see the sounds shared by users ! Enjoy ! 

        </p>
    </div>
</section>

</div>

<div>
    <MapSound />
</div>


</template>

<script>
import MapSound from '../../components/Map.vue';

export default {
    name: 'SoundMap',
    components: {
        MapSound,
    }
  }
</script>