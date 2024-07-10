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

        <div>
            <h1 class="title has-text-centered">Latest News</h1>
            <div class="columns is-multiline">
                <div class="column is-one-third" v-for="article in latestArticles" :key="article.id">
                    <ArticleBox :article="article" />
                </div>
            </div>
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