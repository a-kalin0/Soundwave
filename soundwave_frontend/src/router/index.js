import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/Others/HomeView.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/Others/AboutView.vue')
  },
  {
    path: '/privacy',
    name: 'Privacy',
    component: () => import('../views/Others/PrivacyView.vue')
  },
  {
    path: '/terms',
    name: 'Terms',
    component: () => import('../views/Others/TermsView.vue')
  },
  {
    path: '/cookies',
    name: 'Cookies',
    component: () => import('../views/Others/CookiesView.vue')
  },
  {
    path: '/accessibility',
    name: 'Accessibility',
    component: () => import('../views/Others/AccessibilityView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/Accounts/SignUp.vue')
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: () => import('../views/Accounts/LogIn.vue')
  },
  {
    path: '/account',
    name: 'Account',
    component: () => import('../views/Accounts/AccountView.vue'),
    meta: {
      requireLogin: true,
    }
  },

  {
    path: '/sound-meter',
    name: 'SoundMeter',
    component: () => import('../views/Soundmeter/SoundMeter.vue')
  },
  {
    path: '/my-sounds',
    name: 'MySounds',
    component: () => import('../views/Soundmeter/MySounds.vue')
  },

  {
    path: '/sound-news',
    name: 'SoundNews',
    component: () => import('../views/Soundnews/SoundNews.vue')
  },
  {
    path: '/:category_slug/:article_slug/',
    name: 'Article',
    component: () => import('../views/Soundnews/Article.vue')
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: () => import('../views/Soundnews/Category.vue')
  },
  {
    path: '/sound-map',
    name: 'SoundMap',
    component: () => import('../views/Soundmap/SoundMap.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'PageNotFound',
    component: () => import('../components/Error404.vue')
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
