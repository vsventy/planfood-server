import uuid as uuid_lib

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel


class AgeCategory(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    sort = models.IntegerField(verbose_name=_('Sort'), blank=True, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        ordering = ['sort', 'name']
        verbose_name_plural = _('Age categories')
        verbose_name = _('Age category')

    def __str__(self):
        return self.name


class Group(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    sort = models.IntegerField(verbose_name=_('Sort'), blank=True, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        ordering = ['sort', 'name']
        verbose_name_plural = _('Groups')
        verbose_name = _('Group')

    def __str__(self):
        return self.name


class DishType(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    sort = models.IntegerField(verbose_name=_('Sort'), blank=True, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        ordering = ['sort', 'name']
        verbose_name_plural = _('Dish types')
        verbose_name = _('Dish type')

    def __str__(self):
        return self.name


class ProductCategory(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    sort = models.IntegerField(verbose_name=_('Sort'), blank=True, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        ordering = ['sort', 'name']
        verbose_name_plural = _('Product categories')
        verbose_name = _('Product category')

    def __str__(self):
        return self.name


class DefaultSettings(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    director_initials = models.CharField(verbose_name=_('Director initials'), max_length=255)
    nurse_post = models.CharField(verbose_name=_('Nurse post'), max_length=255)
    nurse_initials = models.CharField(verbose_name=_('Nurse initials'), max_length=255)
    senior_nurse_post = models.CharField(verbose_name=_('Senior nurse post'), max_length=255)
    senior_nurse_initials = models.CharField(verbose_name=_('Senior nurse initials'), max_length=255)
    storekeeper_initials = models.CharField(verbose_name=_('Storekeeper initials'), max_length=255)

    class Meta:
        verbose_name_plural = _('Default Settings')
        verbose_name = _('Default Settings')

    def __str__(self):
        return '%s, %s, %s' % (self.director_initials, self.nurse_initials, self.senior_nurse_initials)
