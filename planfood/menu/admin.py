from datetime import datetime

from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

from planfood.common.models import Group
from planfood.menu.models import DishItem

from .models import MenuDay, NumberOfPersons


class DishItemInline(admin.TabularInline):
    model = DishItem
    fields = ('period', 'dishes')
    filter_horizontal = ('dishes',)


class NumberOfPersonsInline(admin.TabularInline):
    model = NumberOfPersons
    fields = ('group', 'age_category', 'value', 'value_2')


@admin.register(MenuDay)
class MenuDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'group_name', 'dishes_count', 'status')
    readonly_fields = ('status_changed',)
    change_list_template = "admin/menu_change_list.html"
    inlines = [NumberOfPersonsInline, DishItemInline]

    def get_urls(self):
        urls = super(MenuDayAdmin, self).get_urls()
        my_urls = [path('create/', self.create_menu_day, name='menuday')]
        return my_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['group_list'] = Group.objects.values('id', 'name')
        return super(MenuDayAdmin, self).changelist_view(
            request, extra_context=extra_context
        )

    def group_name(self, obj):
        return obj.numbers_of_persons.all().values_list('group__name').first()

    def dishes_count(self, obj):
        value_list = []
        for period in DishItem.PERIOD:
            id_period, _ = period
            q = obj.dish_items.filter(period=id_period).aggregate(Count('dishes'))
            value_list.append(q['dishes__count'])

        return ' / '.join(map(str, value_list))

    def create_menu_day(self, request):
        if request.method == 'POST':
            answer = request.POST.get('group')
            date = request.POST.get('date')
            if answer is not None:
                try:
                    id_group = int(answer)
                    group = Group.objects.get(pk=id_group)
                    menu_day = MenuDay.objects.create(date=datetime.strptime(date, '%d.%m.%Y'))
                    for age_category in group.age_categories.iterator():
                        NumberOfPersons.objects.create(
                            age_category=age_category, group=group, menu_day=menu_day
                        )
                except ValueError:
                    raise ValidationError(
                        "Invalid group_pk value: {0}".format(escape(answer))
                    )
                except Group.DoesNotExist:
                    raise ValidationError(
                        "No object matching group PK {1} exists.".format(escape(answer))
                    )
                self.message_user(
                    request, "Меню-день для групи \"{}\" створений.".format(group.name)
                )
            else:
                self.message_user(
                    request,
                    "Виберіть, будь ласка, групу перебування!",
                    messages.WARNING,
                )
        return HttpResponseRedirect("../")

    group_name.short_description = _('Group')  # type: ignore
    dishes_count.short_description = _('Count of Dishes by period')  # type: ignore
