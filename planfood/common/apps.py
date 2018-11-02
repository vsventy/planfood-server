from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommonConfig(AppConfig):
    name = 'planfood.common'
    verbose_name = _('Common')
