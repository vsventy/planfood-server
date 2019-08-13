import logging
from datetime import datetime

from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.core.serializers import serialize
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.html import escape, format_html
from django.utils.translation import ugettext_lazy as _

from planfood.common.models import DefaultSettings, Group
from planfood.menu.models import DishItem

from .models import MenuDay, NumberOfPersons
from .views import create_menu_report_xlsx

logger = logging.getLogger(__name__)


class DishItemInline(admin.TabularInline):
    model = DishItem
    extra = 0
    fields = ('period', 'dishes')
    filter_horizontal = ('dishes',)


class NumberOfPersonsInline(admin.TabularInline):
    model = NumberOfPersons
    extra = 0
    fields = ('group', 'age_category', 'value')


@admin.register(MenuDay)
class MenuDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'group_name', 'dishes_count', 'status', 'menuday_actions')
    fields = ('date', 'status', 'status_changed')
    readonly_fields = ('status_changed',)
    change_list_template = "admin/menu_change_list.html"
    inlines = [NumberOfPersonsInline, DishItemInline]

    def menuday_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">{}</a>',
            reverse('admin:menu_report', args=[obj.pk]),
            _('Menu/Demand'),
        )

    def get_urls(self):
        urls = super(MenuDayAdmin, self).get_urls()
        my_urls = [
            path('create/', self.create_menu_day, name='menuday'),
            path(
                '<int:menuday_id>/report/',
                view=create_menu_report_xlsx,
                name='menu_report',
            ),
        ]
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
                    menu_day = MenuDay.objects.create(
                        date=datetime.strptime(date, '%d.%m.%Y'),
                        settings=serialize('json', DefaultSettings.objects.all()),
                    )
                    for age_category in group.age_categories.iterator():
                        NumberOfPersons.objects.create(
                            age_category=age_category, group=group, menu_day=menu_day
                        )
                    for period in DishItem.PERIOD:
                        (period_value, period_name) = period
                        DishItem.objects.create(menu_day=menu_day, period=period_value)

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
    menuday_actions.short_description = _('Actions')  # type: ignore
