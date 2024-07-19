<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title" v-if="user">Welcome back {{ user.username }} !! </h1>
                
            </div>

            <div class="column is-6" v-if="user">
                <h1 class="title">Profile settings</h1>
                <p><strong>Username:</strong> {{ user.username }}</p>
                <p><strong>Email:</strong> {{ user.email }}</p>
                <p><strong>ID:</strong> {{ user.id }}</p>
            </div>
            <div class="column is-6" v-else>
                <p>Loading...</p>
            </div>
            <div class="column is-6" v-if="stats">
                <h1 class="title">Statistics</h1>
                <p><strong>Time spent on Soundwave : {{ formatTime(stats.time_spent) }}</strong></p>
                <p><strong>Sounds recorded : {{ stats.sounds_recorded }}</strong></p>
                <p><strong>Sounds shared in the map : {{ stats.sounds_shared }}</strong></p>
            </div>
            <div class="column is-6" v-else>
                <p>Loading...</p>
            </div>

            <hr>
        </div>

        <div class="grid">
            <router-link to="/change-password" class="cell button is-info">Change Password</router-link>
            <div @click="logout" class="cell button is-warning">Log out</div>
            <div @click="showDeactivateModal" class="cell button is-danger">Deactivate Account</div>
            <div @click="showDeleteModal" class="cell button is-danger">Delete Account</div>
            <div class="cell button is-info">Activate 2FA</div>
        </div>

        <!-- Deactivate Account Modal -->
         <div class="modal" :class="{'is-active': isDeactivateModalActive}">
            <div class="modal-background"></div>
            <div class="modal-content">
                <div class="box">
                    <p>You're about to deactivate your account. If you want to reactivate it, check your emails.</p>
                    <button @click="deactivateAccount" class="button is-danger">Deactivate</button>
                    <button @click="hideDeactivateModal" class="button">Cancel</button>
                </div>
            </div>
            <button @click="hideDeactivateModal" class="modal-close is-large" aria-label="close"></button>
         </div>

        <!-- Delete Account Modal -->
         <div class="modal" :class="{ 'is-active': isDeleteModalActive }">
            <div class="modal-background"></div>
            <div class="modal-content">
                <div class="box">
                    <p>Are you sure you want to delete your account ? This action cannot be undone.</p>
                    <button @click="deleteAccount" class="button is-danger">Delete my account</button>
                    <button @click="hideDeleteModal" class="button">Cancel</button>
                </div>
            </div>
            <button @click="hideDeleteModal" class="modal-close is-large" aria-label="close"></button>
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
            errors: [],
            stats: {},
            isDeleteModalActive: false,
            isDeactivateModalActive: false,
        }
    },
    computed: {
        ...mapState(['user'])
    },
    mounted() {
        document.title = 'My account'
        this.fetchUser()
        this.getStats()
    },
    methods: {
        ...mapMutations(['removeToken', 'setUser']),
        showDeleteModal() {
            this.isDeleteModalActive = true
        },
        showDeactivateModal() {
            this.isDeactivateModalActive = true
        },
        hideDeleteModal() {
            this.isDeleteModalActive = false
        },
        hideDeactivateModal() {
            this.isDeactivateModalActive = false
        },
        async getStats() {
            try {
                const response = await axios.get('/api/v1/get_stats/')
                this.stats = response.data
            } catch (error) {
                console.error('Error getting stats:', error)
            }
        },
        async deactivateAccount() {
            try {
                const token = localStorage.getItem("token")
                axios.defaults.headers.common["Authorization"] = `Token ${token}`
                
                await axios.post("/api/v1/deactivate-account/")

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
        async deleteAccount() {
            try {
                const token = localStorage.getItem("token")
                axios.defaults.headers.common["Authorization"] = `Token ${token}`

                await axios.delete("/api/v1/delete-account")

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
        },
        formatTime(seconds) {
            const days = Math.floor(seconds / 86400)
            const hours = Math.floor((seconds % 86400) / 3600)
            const minutes = Math.floor((seconds % 3600) / 60)
            const sec = Math.floor(seconds % 60)
            return `${days}d ${hours}h ${minutes} ${sec}s`
        }
    }
}
</script>

<style scoped>
.page-my-account {
  margin: 20px 20px;
  padding: 20px 20px;
}
</style>
