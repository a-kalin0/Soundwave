<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log in</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Log in</button>
                        </div>
                    </div>

                    <hr>

                    Or <router-link to="/sign-up">click here</router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In | Djackets'
    },
    methods: {
        async submitForm() {
            this.errors = []

            const formData = {
                username: this.username,
                password: this.password
            }

            try {
                const response = await axios.post("/api/v1/token/login/", formData)
                const token = response.data.auth_token

                console.log('Token:', token)
                this.$store.commit('setToken', token)
                localStorage.setItem("token", token)

                // Configurer les en-têtes d'authentification
                axios.defaults.headers.common["Authorization"] = "Token " + token

                // Récupérer les informations de l'utilisateur
                const userResponse = await axios.get('/api/v1/users/me/')
                const user = userResponse.data
                console.log('User:', user)
                this.$store.commit('setUser', user)
                localStorage.setItem('user', JSON.stringify(user))

                const toPath = this.$route.query.to || '/'
                this.$router.push(toPath)
            } catch (error) {
                if (error.response) {
                    for (const property in error.response.data) {
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }
                } else {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(JSON.stringify(error))
                }
            }
        }
    }
}
</script>
