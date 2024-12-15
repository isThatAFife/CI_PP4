from django.apps import AppConfig


class GamelibraryConfig(AppConfig):
    """
    Configuration class for the 'gamelibrary' Django app.
    Specifies the default auto field and the app name.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "gamelibrary"
