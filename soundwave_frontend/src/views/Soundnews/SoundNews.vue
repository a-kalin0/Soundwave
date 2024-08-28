<template>
  <div :class="['soundnews-page', themeClass]">
    <!-- Hero section -->
    <section class="hero is-medium mb-6" :class="themeClass">
      <div class="hero-body has-text-centered">
        <p class="title mb-6" :class="themeTextClass">Welcome to the Sound News page!</p>
        <p class="subtitle" :class="themeTextClass">
          Discover the latest news about sound pollution and innovations in sound technology.
        </p>
      </div>
    </section>

    <!-- Barre de recherche -->
    <div class="search-bar mb-5">
      <div class="control has-icons-left has-icons-right">
        <input
          type="text"
          v-model="searchQuery"
          @input="searchArticles"
          placeholder="Search for articles..."
          class="input is-medium"
        />
        <span class="icon is-medium is-left">
          <i class="fas fa-search"></i>
        </span>
      </div>
    </div>

    <!-- Catégories de filtrage -->
    <div class="categories buttons is-centered mb-6">
      <button
        @click="filterByCategory('all')"
        class="button"
        :class="{'is-primary': selectedCategory === 'all'}"
      >
        All
      </button>
      <button
        @click="filterByCategory('Good')"
        class="button is-success"
        :class="{'is-primary': selectedCategory === 'good'}"
      >
        Good News
      </button>
      <button
        @click="filterByCategory('Bad')"
        class="button is-danger"
        :class="{'is-primary': selectedCategory === 'bad'}"
      >
        Bad News
      </button>
      <button
        @click="filterByCategory('Info')"
        class="button is-info"
        :class="{'is-primary': selectedCategory === 'info'}"
      >
        Info
      </button>
    </div>

    <!-- Articles -->
    <div class="articles">
      <h1 class="title has-text-centered" :class="themeTextClass">Latest News</h1>
      <div class="columns is-multiline">
        <div
          class="column is-one-third"
          v-for="article in filteredArticles"
          :key="article.id"
        >
          <ArticleBox :article="article" />
        </div>
      </div>
      <div v-if="filteredArticles.length === 0" class="has-text-centered mt-5">
        <p class="subtitle" :class="themeTextClass">No articles found matching your search or category.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ArticleBox from '@/components/ArticleBox.vue';
import { mapState } from 'vuex';

export default {
  name: 'SoundNews',
  components: {
    ArticleBox
  },
  data() {
    return {
      latestArticles: [],
      searchQuery: '',
      selectedCategory: 'all',
    };
  },
  computed: {
    ...mapState(['theme']),
    themeClass() {
      return this.theme === 'dark' ? 'is-dark' : 'is-light';
    },
    themeTextClass() {
      return this.theme === 'dark' ? 'has-text-white' : 'has-text-black';
    },
    // Articles filtrés par catégorie et recherche
    filteredArticles() {
      return this.latestArticles.filter(article => {
        const matchesCategory =
          this.selectedCategory === 'all' ||
          article.category === this.selectedCategory;
        
        const titleExists = article.title && typeof article.title === 'string';
        const summaryExists = article.summary && typeof article.summary === 'string';

        const matchesSearch =
          (titleExists && article.title.toLowerCase().includes(this.searchQuery.toLowerCase())) ||
          (summaryExists && article.summary.toLowerCase().includes(this.searchQuery.toLowerCase()));

        return matchesCategory && matchesSearch;
      });
    }
  },
  mounted() {
    this.getLatestArticles();
    document.title = this.$t('soundNews');
  },
  methods: {
    async getLatestArticles() {
      try {
        const response = await axios.get('/api/v1/latest_articles');
        this.latestArticles = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    filterByCategory(category) {
      this.selectedCategory = category;
    },
    searchArticles() {
      // Les articles sont automatiquement filtrés grâce à la propriété calculée
    }
  }
};
</script>

<style scoped>
.soundnews-page {
  padding: 20px;
}

.search-bar {
  max-width: 600px;
  margin: 0 auto;
}

.categories {
  margin-bottom: 20px;
}

.articles .columns {
  justify-content: center;
}

.article-card {
  transition: transform 0.2s ease;
}

.article-card:hover {
  transform: translateY(-10px);
}
</style>
