import uuid as uuid_lib

from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import StatusModel, TimeStampedModel

from planfood.common.models import AgeCategory, Group


class MenuDay(StatusModel, TimeStampedModel):
    STATUS = Choices(('draft', _('draft')), ('published', _('published')))
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    date = models.DateField(verbose_name=_('Date'))
    status = StatusField(verbose_name=_('Status'))
    settings = JSONField(blank=True, null=True, verbose_name=_('Settings'))

    class Meta:
        ordering = ['-date']
        verbose_name_plural = _('Menu days')
        verbose_name = _('Menu day')

    def __str__(self):
        return str(self.date)

    @property
    def group(self):
        return self.numbers_of_persons.first().group


class NumberOfPersons(TimeStampedModel):
    age_category = models.ForeignKey(
        AgeCategory,
        verbose_name=_('Age category'),
        blank=True,
        null=True,
        related_name='numbers_of_persons',
        on_delete=models.SET_NULL,
    )
    group = models.ForeignKey(
        Group,
        verbose_name=_('Group'),
        blank=True,
        null=True,
        related_name='numbers_of_persons',
        on_delete=models.SET_NULL,
    )
    menu_day = models.ForeignKey(
        MenuDay,
        verbose_name=_('Menu day'),
        related_name='numbers_of_persons',
        on_delete=models.CASCADE,
    )
    value = models.IntegerField(
        verbose_name=_('Value'),
        blank=True,
        default=0,
        help_text=_('A total number of persons / A number of persons as day stay'),
    )
    value_2 = models.IntegerField(
        verbose_name=_('Value 2'),
        blank=True,
        default=0,
        help_text=_('A number of persons as outpatient'),
    )

    class Meta:
        verbose_name_plural = _('Numbers of persons')
        verbose_name = _('Number of persons')

    def __str__(self):
        return '%s (%s)' % (self.menu_day, self.value)


class DishItem(TimeStampedModel):
    PERIOD = Choices(
        (0, 'breakfast', _('Breakfast')),
        (1, 'after_breakfast', '10:35 / 11:00'),
        (2, 'lunch', _('Lunch')),  # old value: 1
        (3, 'after_lunch', '15:00 / 15:45'),  # old value: 2
        (4, 'dinner', _('Dinner')),  # old value: 3
        (5, 'tea', _('Tea')),  # old value: 4
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
        'dishes.Dish', verbose_name=_('Dishes'), blank=True, related_name='dish_items'
    )
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    period = models.IntegerField(verbose_name=_('Period'), choices=PERIOD)

    class Meta:
        verbose_name_plural = _('Set of dishes')
        verbose_name = _('Dish item')

    def __str__(self):
        return '%s (%s)' % (self.menu_day.date, self.PERIOD[self.period])
