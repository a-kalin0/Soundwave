import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    user: null,
    isLoading: false
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user = JSON.parse(localStorage.getItem('user'))
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user = null
      }
      console.log('Initialized store:', state)
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    setUser(state, user) {
      state.user = user
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
      state.user = null
    }
  },
  actions: {
    async logIn({ commit }, credentials) {
      try {
        const response = await axios.post('/api/v1/token/login/', credentials)
        const token = response.data.auth_token
        commit('setToken', token)
        localStorage.setItem('token', token)

        axios.defaults.headers.common['Authorization'] = `Token ${token}`
        const userResponse = await axios.get('/api/v1/users/me/')
        const user = userResponse.data
        commit('setUser', user)
        localStorage.setItem('user', JSON.stringify(user))
        console.log('User logged in:', user)
      } catch (error) {
        console.error('Error during login:', error)
      }
    },
    logOut({ commit }) {
      commit('removeToken')
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  modules: {}
})
