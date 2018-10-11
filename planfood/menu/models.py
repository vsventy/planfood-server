import uuid as uuid_lib

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import StatusModel, TimeStampedModel

from planfood.common.models import AgeCategory, Group


class MenuDay(StatusModel, TimeStampedModel):
    STATUS = Choices('draft', 'published')
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    date = models.DateField()
    status = StatusField()

    class Meta:
        verbose_name_plural = _('Menu days')
        verbose_name = _('Menu day')

    def __str__(self):
        return str(self.date)


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
    value = models.IntegerField(verbose_name=_('Value'), blank=True, default=0)

    class Meta:
        verbose_name_plural = _('Numbers of persons')
        verbose_name = _('Number of persons')

    def __str__(self):
        return '%s (%s)' % (self.menu_day, self.value)
