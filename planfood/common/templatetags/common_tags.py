import time
import os

from django import template

from planfood import __version__

register = template.Library()


@register.simple_tag
def version_date():
    return time.strftime('%d.%m.%Y', time.gmtime(os.path.getmtime('.git')))


@register.simple_tag
def version_number():
    return __version__
