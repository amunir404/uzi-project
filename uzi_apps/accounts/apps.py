from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uzi_apps.accounts'
    
    def ready(self):
        import uzi_apps.accounts.signals
