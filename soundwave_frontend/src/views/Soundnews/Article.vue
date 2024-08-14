<template>
    <div class="page-article">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <img v-bind:src="article.get_image">
                </figure>

                <h1 class="title">{{ article.title }}</h1>

                <p>{{ article.content }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ArticleVue',
    data() {
        return {
            article: {},
        }
    },
    mounted() {
        this.getArticle()
    },
    methods: {
        async getArticle() {

            const category_slug = this.$route.params.category_slug
            const article_slug = this.$route.params.article_slug
        
            try {
                await axios
                    .get(`/api/v1/articles/${category_slug}/${article_slug}`)
                    .then(response => {
                        this.article = response.data;
                        
                        document.title = this.article.title
                    })
            }catch(error){ 
                console.log(error);
            }
        }
    }
}
</script>