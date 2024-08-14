import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import axios from 'axios'
import i18n from '@/plugins/i18n';
import FlagIcon from 'vue-flag-icon'


axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(store).use(router, axios).use(i18n).use(FlagIcon).mount('#app')

