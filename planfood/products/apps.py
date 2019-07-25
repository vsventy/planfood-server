from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProductsConfig(AppConfig):
    name = 'planfood.products'
    verbose_name = _('Products')
