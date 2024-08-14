from djoser import email

class CustomActivationEmail(email.ActivationEmail):
    def get_context_data(self):
        context = super().get_context_data()
        context['protocol'] = 'http'
        context['domain'] = 'localhost:8080'  # Changez cela pour le domaine de votre frontend
        return context

class CustomPasswordResetEmail(email.PasswordResetEmail):
    def get_context_data(self):
        context = super().get_context_data()
        context['protocol'] = 'http'
        context['domain'] = 'localhost:8080'  # Changez cela pour le domaine de votre frontend
        return context   