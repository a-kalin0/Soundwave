<template>
    <div class="page-article">
      <section class="hero is-medium is-primary mb-6">
        <div class="hero-body has-text-centered">
          <h1 class="title">{{ article.title }}</h1>
          <p class="subtitle">{{ article.publication_date }} | {{ article.category }}</p>
        </div>
      </section>
  
      <div class="container">
        <div class="columns">
          <div class="column is-9">
            <figure class="image mb-6">
              <img v-bind:src="article.get_image" alt="Article image">
            </figure>
  
            <div class="content">
              <p v-html="article.content"></p>
            </div>
  
            <hr>
  
            <div class="tags">
              <span class="tag is-link" v-for="tag in article.tags" :key="tag">{{ tag }}</span>
            </div>
          </div>
  
          <div class="column is-3">
            <div class="box">
              <h2 class="subtitle">Article Details</h2>
              <p><strong>Author:</strong> {{ article.author }}</p>
              <p><strong>Published:</strong> {{ article.publication_date }}</p>
              <p><strong>Category:</strong> {{ article.category }}</p>
            </div>
  
          </div>
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
      };
    },
    mounted() {
      this.getArticle();
      document.title = 'Lol';
    },
    methods: {
      async getArticle() {
        const category_slug = this.$route.params.category_slug;
        const article_slug = this.$route.params.article_slug;
  
        try {
          const response = await axios.get(`/api/v1/articles/${category_slug}/${article_slug}`);
          this.article = response.data;
          document.title = this.article.title;
        } catch (error) {
          console.log(error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .page-article {
    margin-top: 20px;
  }
  .content {
    font-size: 1.2rem;
    line-height: 1.6;
  }
  
  .tags {
    margin-top: 20px;
  }
  </style>
  