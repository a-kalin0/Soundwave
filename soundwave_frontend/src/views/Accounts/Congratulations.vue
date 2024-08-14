<template>
    <div class="congratulations-page">
        <div class="container">
            <h1 class="title">Congratulations!</h1>
            <p>Your account has been created successfully. Please check your email to activate your account.</p>
            <button class="button is-primary" @click="resendActivationEmail">Resend Activation Email</button>
            <div v-if="status === 'loading'" class="notification is-info">
                Sending activation email, please wait...
            </div>
            <div v-if="status === 'success'" class="notification is-success">
                Activation email sent successfully!
            </div>
            <div v-if="status === 'error'" class="notification is-danger">
                There was an error sending the activation email. Please try again later.
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CongratulationsView',
    data() {
        return {
            status: '' // 'loading', 'success', 'error'
        }
    },
    methods: {
        async resendActivationEmail() {
            this.status = 'loading'
            try {
                await axios.post('/api/v1/users/resend_activation/', {
                    email: this.$route.query.email
                })
                this.status = 'success'
                this.$router.push({ name: 'home' })
            } catch (error) {
                this.status = 'error'
                console.error('Error resending activation email:', error)
            }
        }
    }
}
</script>

<style scoped>
.congratulations-page {
    margin-top: 50px;
    text-align: center;
}
</style>
