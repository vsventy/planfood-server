from django.contrib import admin

from .models import Dish, DishItem, Output


class OutputInline(admin.TabularInline):
    model = Output


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    inlines = [OutputInline]


@admin.register(DishItem)
class DishItemAdmin(admin.ModelAdmin):
    list_display = ('menu_day', 'period')


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ('dish', 'age_category', 'group', 'value')
