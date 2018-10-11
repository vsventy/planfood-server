from django.contrib import admin

from planfood.dishes.models import DishItem

from .models import MenuDay, NumberOfPersons


class DishItemInline(admin.TabularInline):
    model = DishItem


class NumberOfPersonsInline(admin.TabularInline):
    model = NumberOfPersons


@admin.register(MenuDay)
class MenuDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'status')
    readonly_fields = ('status_changed',)
    inlines = [NumberOfPersonsInline, DishItemInline]


@admin.register(NumberOfPersons)
class NumberOfPersonsAdmin(admin.ModelAdmin):
    list_display = ('menu_day', 'age_category', 'group', 'value')
