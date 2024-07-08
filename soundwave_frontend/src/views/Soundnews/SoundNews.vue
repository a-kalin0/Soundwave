<template>
    <div class="home">

        <section class="hero is-medium is-dark mb-6">
            <div class="hero-body has-text-centered">
                <p class="title mb-6">
                    Welcome to the Sound News page !
                </p>
                <p class="subtitle">
                    Here you can see the news about sound pollution ! Enjoy ! 

                </p>
            </div>
        </section>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">
                    Latest News
                </h2>
            </div>

            <ArticleBox v-for="article in latestArticles" v-bind:key="article.id" v-bind:article="article" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import ArticleBox from '@/components/ArticleBox.vue'

export default {
    name: 'SoundNews',
    data() {
        return {
            latestArticles: []
        }
    },
    components: {
        ArticleBox
    },
    mounted() {
        this.getLatestArticles()

        document.title = 'Soundnews'
    },
    methods: {
        async getLatestArticles() {
            try {
                await axios
                    .get('/api/v1/latest_articles')
                    .then(response => {
                        this.latestArticles = response.data
                    })
            } catch (error) {
                console.error(error)
            }
        }
    }
}
</script>