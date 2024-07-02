import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/privacy',
    name: 'Privacy',
    component: () => import('../views/PrivacyView.vue')
  },
  {
    path: '/terms',
    name: 'Terms',
    component: () => import('../views/TermsView.vue')
  },
  {
    path: '/cookies',
    name: 'Cookies',
    component: () => import('../views/CookiesView.vue')
  },
  {
    path: '/accessibility',
    name: 'Accessibility',
    component: () => import('../views/AccessibilityView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: () => import('../views/LogIn.vue')
  },
  {
    path: '/account',
    name: 'Account',
    component: () => import('../views/AccountView.vue')
  },

  {
    path: '/sound-meter',
    name: 'SoundMeter',
    component: () => import('../views/SoundMeter.vue')
  },
  {
    path: '/sound-news',
    name: 'SoundNews',
    component: () => import('../views/SoundNews.vue')
  },
  {
    path: '/sound-map',
    name: 'SoundMap',
    component: () => import('../views/SoundMap.vue')
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
