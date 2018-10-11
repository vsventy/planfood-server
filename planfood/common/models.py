import uuid as uuid_lib

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class AgeCategory(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Age categories')
        verbose_name = _('Age category')

    def __str__(self):
        return self.name


class Group(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = _('Groups')
        verbose_name = _('Group')

    def __str__(self):
        return self.name
