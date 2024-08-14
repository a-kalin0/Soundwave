<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <img :src="article.get_thumbnail" alt="Article Thumbnail">
            </figure>
        </div>
        <div class="card-content">
            <h3 class="is-size-4">{{ article.title }}</h3>
            <p>{{ article.author }}</p>
            <router-link :to="article.get_absolute_url" class="button is-dark mt-4">View details</router-link>
            <router-link
                :to="'/category/' + article.category"
                :class="categoryClass(article.category)"
                class = "button mt-4"
            >{{ article.category }}</router-link>

            
        </div>
    </div>
</template>

<script>
export default {
    name: 'ArticleBox',
    props: {
        article: Object
    },
    methods: {
        categoryClass(categoryName) {
            switch(categoryName.toLowerCase()) {
                case 'bad':
                    return 'is-danger';
                case 'good':
                    return 'is-success';
                case 'info':
                    return 'is-info';
                default:
                    return '';
            }
        }
    }
}
</script>

<style scoped>
.card {
    margin: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.card-content {
    flex-grow: 1;
}
</style>