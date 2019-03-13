from django.contrib import admin

from planfood.menu.models import DishItem

from .models import MenuDay, NumberOfPersons


class DishItemInline(admin.TabularInline):
    model = DishItem
    fields = ('period', 'dishes')
    filter_horizontal = ('dishes',)
    min_num = 5
    extra = 0


class NumberOfPersonsInline(admin.TabularInline):
    model = NumberOfPersons
    fields = ('group', 'age_category', 'value')
    min_num = 5
    extra = 0


@admin.register(MenuDay)
class MenuDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'status')
    readonly_fields = ('status_changed',)
    inlines = [NumberOfPersonsInline, DishItemInline]
