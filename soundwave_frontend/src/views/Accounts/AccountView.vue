<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Account</h1>
                
            </div>

            <div class="column is-12" v-if="user">
                <h1 class="title">Hello {{ user.username }} !!</h1>
                <p><strong>Username:</strong> {{ user.username }}</p>
                <p><strong>Email:</strong> {{ user.email }}</p>
                <p><strong>ID:</strong> {{ user.id }}</p>
            </div>
            <div class="column is-12" v-else>
                <p>Loading...</p>
            </div>

            <div class="column is-12">
                <button @click="logout" class="button is-danger">Log out</button>
            </div>

            <hr>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapMutations } from 'vuex'

export default {
    name: 'MyAccount',
    data() {
        return {
            errors: []
        }
    },
    computed: {
        ...mapState(['user'])
    },
    mounted() {
        document.title = 'My account'
        this.fetchUser()
    },
    methods: {
        ...mapMutations(['removeToken', 'setUser']),
        async logout() {
            try {
                const token = localStorage.getItem("token")
                axios.defaults.headers.common["Authorization"] = `Token ${token}`

                await axios.post("/api/v1/token/logout/")

                localStorage.removeItem("token")
                localStorage.removeItem("user")

                axios.defaults.headers.common["Authorization"] = ""

                this.removeToken()

                this.$router.push('/')
            } catch (error) {
                if (error.response) {
                    for (const property in error.response.data) {
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }
                } else {
                    this.errors.push('Something went wrong. Please try again')
                    console.error(error)
                }
            }
        },
        async fetchUser() {
            try {
                const response = await axios.get('/api/v1/users/me/')
                const user = response.data
                this.setUser(user)
                localStorage.setItem('user', JSON.stringify(user))
            } catch (error) {
                console.error('Error fetching user:', error)
            }
        }
    }
}
</script>

<style scoped>
.page-my-account {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
</style>
