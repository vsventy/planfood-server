import uuid as uuid_lib
from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from planfood.common.models import AgeCategory, DishType, Group
from planfood.products.models import Product


class Dish(TimeStampedModel):
    products = models.ManyToManyField(
        Product, verbose_name=_('Products'), blank=True, related_name='dishes'
    )
    dish_type = models.OneToOneField(
        DishType,
        verbose_name=_('Dish type'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        verbose_name_plural = _('Dishes')
        verbose_name = _('Dish')

    def __str__(self):
        return self.name


class Output(TimeStampedModel):
    age_category = models.ForeignKey(
        AgeCategory,
        verbose_name=_('Age category'),
        blank=True,
        null=True,
        related_name='outputs',
        on_delete=models.SET_NULL,
    )
    group = models.ForeignKey(
        Group,
        verbose_name=_('Group'),
        blank=True,
        null=True,
        related_name='outputs',
        on_delete=models.SET_NULL,
    )
    dish = models.ForeignKey(
        Dish,
        verbose_name=_('Dish'),
        blank=True,
        null=True,
        related_name='outputs',
        on_delete=models.SET_NULL,
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    value = models.CharField(verbose_name=_('Value'), max_length=20)

    class Meta:
        verbose_name_plural = _('Output values')
        verbose_name = _('Output value')

    def __str__(self):
        return '%s (%s)' % (self.dish.name, self.value)


class Norm(TimeStampedModel):
    dish = models.ForeignKey(
        Dish,
        verbose_name=_('Dish'),
        related_name='norms',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_('Product'),
        blank=True,
        null=True,
        related_name='norms',
        on_delete=models.SET_NULL
    )
    age_category = models.ForeignKey(
        AgeCategory,
        verbose_name=_('Age category'),
        blank=True,
        null=True,
        related_name='norms',
        on_delete=models.SET_NULL,
    )
    group = models.ForeignKey(
        Group,
        verbose_name=_('Group'),
        blank=True,
        null=True,
        related_name='norms',
        on_delete=models.SET_NULL,
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    value = models.DecimalField(
        verbose_name=_('Value'),
        max_digits=10,
        decimal_places=4,
        default=Decimal('0.0000'),
    )

    class Meta:
        verbose_name_plural = _('Norms')
        verbose_name = _('Norm')

    def __str__(self):
        return self.dish.name
