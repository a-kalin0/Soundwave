from djoser import email

class CustomActivationEmail(email.ActivationEmail):
    def get_context_data(self):
        context = super().get_context_data()
        context['protocol'] = 'http'
        context['domain'] = '127.0.0.1:8080'  # Changez cela pour le domaine de votre frontend
        return context
