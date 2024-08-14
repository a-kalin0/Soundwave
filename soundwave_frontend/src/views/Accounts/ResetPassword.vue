<template>
    <div class="reset-password-page">
        <div class="container">
            <h1 class="title">Reset Password</h1>
            <form @submit.prevent="submitEmail">
                <div class="field">
                    <label>Email</label>
                    <div class="control">
                        <input type="email" class="input" v-model="email">
                    </div>
                </div>
                <div class="notification is-danger" v-if="errors.length">
                    <p v-for="error in errors" :key="error">{{ error }}</p>
                </div>
                <div class="field">
                    <div class="control">
                        <button class="button is-dark">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'ResetPasswordRequest',
    data() {
        return {
            email: '',
            errors: []
        }
    },
    methods: {
        async submitEmail() {
            this.errors = []
            try {
                await axios.post('/api/v1/users/reset_password/', { email: this.email })
                this.$router.push('/')
            } catch (error) {
                if (error.response) {
                    for (const property in error.response.data) {
                        this.errors.push(`${property}: ${error.response.data[property]}`)
                    }
                } else {
                    this.errors.push('Something went wrong. Please try again.')
                    console.error(error)
                }
            }
        }
    }
}
</script>

<style scoped>
.reset-password-page {
    margin-top: 50px;
    text-align: center;
}
</style>
