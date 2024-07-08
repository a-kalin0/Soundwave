<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>

            <ArticleBox 
                v-for="article in category.articles"
                v-bind:key="article.id"
                v-bind:product="article" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ArticleBox from '@/components/ArticleBox'

export default {
    name: 'CateGory',
    components: {
        ArticleBox
    },
    data() {
        return {
            category: {
                articles: []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug

            try {axios
                .get(`/api/v1/articles/${categorySlug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name
                })
            }catch(error){
                    console.log(error)
            
                    toast({
                        message: 'Something went wrong. Please try again.',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
            }
        }
    }
}
</script>