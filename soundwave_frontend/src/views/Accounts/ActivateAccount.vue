<template>
    <div class="activation-page">
        <div class="container">
            <div v-if="status === 'loading'" class="notification is-info">
                Activating your account, please wait...
            </div>
            <div v-if="status === 'success'" class="notification is-success">
                Your account has been activated successfully! You can now <router-link to="/login">login</router-link>.
            </div>
            <div v-if="status === 'error'" class="notification is-danger">
                There was an error activating your account. Please try again later.
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ActivateAccount',
    data() {
        return {
            status: 'loading', // 'loading', 'success', 'error'
        }
    },
    mounted() {
        this.activateAccount()
    },
    methods: {
        async activateAccount() {
            const { uid, token } = this.$route.params
            try {
                await axios({
                    method: 'POST',
                    url: '/api/v1/users/activation/',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    data: JSON.stringify({ uid, token })
                })
                this.status = 'success'
            } catch (error) {
                this.status = 'error'
                console.error('Error activating account:', error)
            }
        }
    }
}
</script>

<style scoped>
.activation-page {
    margin-top: 50px;
    text-align: center;
}
</style>
