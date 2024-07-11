<template>
    <div class="change-password-page">
        <div class="container">
            <h1 class="title">Change Password</h1>
            <form @submit.prevent="changePassword">
                <div class="field">
                    <label>Old Password</label>
                    <div class="control">
                        <input type="password" class="input" v-model="oldPassword">
                    </div>
                </div>
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
                        <button class="button is-dark">Change Password</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'ChangePassword',
    data() {
        return {
            oldPassword: '',
            newPassword: '',
            confirmNewPassword: '',
            errors: []
        }
    },
    methods: {
        async changePassword() {
            this.errors = []
            if (this.newPassword !== this.confirmNewPassword) {
                this.errors.push("New passwords do not match.")
                return
            }

            const formData = {
                current_password: this.oldPassword,
                new_password: this.newPassword
            }

            try {
                await axios.post('/api/v1/users/set_password/', formData, {
                    headers: {
                        'Authorization': `Token ${localStorage.getItem('token')}`
                    }
                })
                toast({
                    message: 'Password changed successfully!',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                })
                this.$router.push('/account')
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
.change-password-page {
    margin-top: 50px;
    text-align: center;
}
</style>
