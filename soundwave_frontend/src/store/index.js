import { createStore } from 'vuex'
import Cookies from 'js-cookie'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    user: null,
    theme: 'light', // Valeur par défaut
    language: 'en', // Valeur par défaut
  },
  mutations: {
    initializeStore(state) {

      const token = Cookies.get('token');
      const user = Cookies.get('user');
      const theme = Cookies.get('theme');
      const language = Cookies.get('language');

      if (token) {
        state.token = token;
        state.isAuthenticated = true;
      } else {
        state.token = '';
        state.isAuthenticated = false;
      }
      if (user) {
        state.user = JSON.parse(user);
      }
      if (theme) {
        state.theme = theme;
      }
      if (language) {
        state.language = language;
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
      Cookies.set('token', token, { expires: 7 });
    },
    removeToken(state) {
      state.token = '';
      state.isAuthenticated = false;
      Cookies.remove('token');
      Cookies.remove('user');
    },
    setUser(state, user) {
      state.user = user;
      Cookies.set('user', JSON.stringify(user), { expires: 7 });
    },
    setTheme(state, theme) {
      state.theme = theme;
      Cookies.set('theme', theme, { expires: 7 });
    },
    setLanguage(state, language) {
      state.language = language;
      Cookies.set('language', language, { expires: 7 });
    }
  }
})
