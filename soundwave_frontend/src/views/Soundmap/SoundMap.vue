<template>
    <div class="soundMap" :class="themeClass">
        <section class="hero is-medium mb-6" :class="themeClass">
            <div class="hero-body has-text-centered">
                <p class="title mb-6" :class="themeTextClass">Welcome to the Sound Map page !</p>
                <p class="subtitle" :class="themeTextClass">Here you can see the sounds shared by users ! Enjoy !</p>
            </div>
        </section>
    </div>

    <div class="mapSound">
        <MapSound />
    </div>
</template>

<script>
import MapSound from '../../components/Map.vue';
import { mapState } from 'vuex';

export default {
    name: 'SoundMap',
    components: {
        MapSound,
    },
    computed: {
        ...mapState(['theme']),
        themeClass() {
            return this.theme === 'dark' ? 'is-dark' : 'is-light';
        },
        themeTextClass() {
            return this.theme === 'dark' ? 'has-text-white' : 'has-text-black';
        }
    },
    mounted() {
        document.title = this.$t('soundMap');
    },
}
</script>

<style scoped>

.mapSound {
    color: black;
}

</style>