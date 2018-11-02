from django.contrib import admin

from .models import Dish, Output


class OutputInline(admin.TabularInline):
    model = Output


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    inlines = [OutputInline]


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ('dish', 'age_category', 'group', 'value')
