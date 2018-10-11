import uuid as uuid_lib

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.models import TimeStampedModel

from planfood.common.models import AgeCategory, Group
from planfood.menu.models import MenuDay
from planfood.products.models import Product


class Dish(TimeStampedModel):
    products = models.ManyToManyField(
        Product, verbose_name='Products', blank=True, related_name='dishes'
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        verbose_name_plural = _('Dishes')
        verbose_name = _('Dish')

    def __str__(self):
        return self.name


class DishItem(TimeStampedModel):
    PERIOD = Choices(
        (0, 'breakfast', _('Breakfast')),
        (1, 'lunch', _('Lunch')),
        (2, 'tea', _('Tea')),
        (3, 'dinner', _('Dinner')),
    )
    menu_day = models.ForeignKey(
        MenuDay,
        verbose_name=_('Menu day'),
        blank=True,
        null=True,
        related_name='dish_items',
        on_delete=models.SET_NULL,
    )
    dishes = models.ManyToManyField(
        Dish, verbose_name='Dishes', blank=True, related_name='dish_items'
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    period = models.IntegerField(verbose_name=_('Period'), choices=PERIOD)

    class Meta:
        verbose_name_plural = _('Set of dishes')
        verbose_name = _('Dish item')

    def __str__(self):
        return '%s (%s)' % (self.menu_day.date, self.PERIOD[self.period])


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