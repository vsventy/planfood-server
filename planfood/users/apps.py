from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersAppConfig(AppConfig):

    name = "planfood.users"
    verbose_name = _('Users')

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
