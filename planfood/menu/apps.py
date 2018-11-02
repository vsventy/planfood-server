from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MenuAppConfig(AppConfig):
    name = 'planfood.menu'
    verbose_name = _('Menu')
