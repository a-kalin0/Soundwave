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
    path: '/electronic',
    name: 'electronic',
    component: () => import('../views/Others/ElectronicSoundmeterView.vue')
  },
  {
    path: '/terms',
    name: 'Terms',
    component: () => import('../views/Others/TermsView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/Accounts/SignUp.vue')
  },
  {
    path: '/congratulations',
    name: 'Congratulations',
    component: () => import('../views/Accounts/Congratulations.vue')
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
    path: '/change-password',
    name: 'ChangePassword',
    component: () => import('../views/Accounts/ChangePassword.vue')
  },
  {
    path: '/reset-password',
    name: 'ResetPassword',
    component: () => import('../views/Accounts/ResetPassword.vue'),
    meta: {
      requireLogin: true,
    }
  },
  {
    path: '/password/reset/confirm/:uid/:token',
    name: 'ResetpasswordConfirm',
    component: () => import('../views/Accounts/ResetPasswordConfirm.vue'),
    meta: {
      requireLogin: true,
    }
  },
  {
    path: '/activate/:uid/:token',
    name: 'ActivateAccount',
    component: () => import('../views/Accounts/ActivateAccount.vue')
  },
  {
    path: '/sound-meter',
    name: 'SoundMeter',
    component: () => import('../views/Soundmeter/SoundMeter.vue')
  },
  {
    path: '/my-sounds',
    name: 'MySounds',
    component: () => import('../views/Soundmeter/MySounds.vue'),
    meta: {
      requireLogin: true,
    }
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
