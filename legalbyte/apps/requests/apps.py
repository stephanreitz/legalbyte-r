# AppConfig is Django's base class for application configuration.
from django.apps import AppConfig

# This class identifies the requests application to Django.
class RequestsConfig(AppConfig):
    # The dotted Python path must match the app's location inside apps/.
    name = 'apps.requests'
