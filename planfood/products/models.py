import uuid as uuid_lib
from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.models import TimeStampedModel

from planfood.common.models import AgeCategory, Group, ProductCategory


class Product(TimeStampedModel):
    UNIT = Choices(
        (0, 'kg', _('Kg')),
        (1, 'pcs', _('Pcs')),
        (2, 'jar', _('Jar')),
        (3, 'liter', _('Liter')),
    )

    category = models.ForeignKey(
        ProductCategory,
        verbose_name=_('Product category'),
        blank=True,
        null=True,
        related_name='products',
        on_delete=models.SET_NULL,
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    item_number = models.CharField(
        verbose_name=_('Item number'), unique=True, max_length=100
    )
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    unit = models.IntegerField(verbose_name=_('Unit'), choices=UNIT)
    unit_price = models.DecimalField(
        verbose_name=_('Unit price'),
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
    )
    convert_ratio = models.DecimalField(
        verbose_name=_('Convert ratio'),
        max_digits=10,
        decimal_places=2,
        default=Decimal('1.00'),
    )

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Products')
        verbose_name = _('Product')

    def __str__(self):
        return '%s - %s' % (self.item_number, self.name)


class Norm(TimeStampedModel):
    product_category = models.ForeignKey(
        ProductCategory,
        verbose_name=_('Product category'),
        blank=True,
        null=True,
        related_name='product_norms',
        on_delete=models.SET_NULL,
    )
    age_category = models.ForeignKey(
        AgeCategory,
        verbose_name=_('Age category'),
        blank=True,
        null=True,
        related_name='product_norms',
        on_delete=models.SET_NULL,
    )
    group = models.ForeignKey(
        Group,
        verbose_name=_('Group'),
        blank=True,
        null=True,
        related_name='product_norms',
        on_delete=models.SET_NULL,
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    value = models.DecimalField(
        verbose_name=_('Value'),
        max_digits=10,
        decimal_places=5,
        default=Decimal('0.00000'),
    )

    class Meta:
        verbose_name_plural = _('Norms')
        verbose_name = _('Norm')

    def __str__(self):
        return self.product_category.name
