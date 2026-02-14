from datetime import date

from django import forms
from django.utils.translation import ugettext_lazy as _

from planfood.common.models import Group
from planfood.common.widgets import MonthYearWidget


class NormsAnalysisForm(forms.Form):
    month = forms.DateField(
        label=_('Month / Year'), required=True, widget=MonthYearWidget()
    )
    group = forms.ModelChoiceField(
        label=_('Group'), required=True, queryset=Group.objects.all()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        year = date.today().year
        self.fields['month'].widget = MonthYearWidget(years=range(year - 2, year + 3))
