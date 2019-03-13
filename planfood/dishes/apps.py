from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DishesConfig(AppConfig):
    name = 'planfood.dishes'
    verbose_name = _('Card of dishes')
