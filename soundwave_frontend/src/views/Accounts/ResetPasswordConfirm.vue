<template>
    <div class="reset-password-confirm-page">
        <div class="container">
            <h1 class="title">Set New Password</h1>
            <form @submit.prevent="submitNewPassword">
                <div class="field">
                    <label>New Password</label>
                    <div class="control">
                        <input type="password" class="input" v-model="newPassword">
                    </div>
                </div>
                <div class="field">
                    <label>Confirm New Password</label>
                    <div class="control">
                        <input type="password" class="input" v-model="confirmNewPassword">
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
    name: 'ResetPasswordConfirm',
    data() {
        return {
            newPassword: '',
            confirmNewPassword: '',
            errors: []
        }
    },
    methods: {
        async submitNewPassword() {
            this.errors = []
            const { uid, token } = this.$route.params
            if (this.newPassword !== this.confirmNewPassword) {
                this.errors.push("Passwords do not match.")
                return
            }
            try {
                await axios.post('/api/v1/users/reset_password_confirm/', {
                    uid,
                    token,
                    new_password: this.newPassword
                })
                this.$router.push('/log-in')
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
.reset-password-confirm-page {
    margin-top: 50px;
    text-align: center;
}
</style>
