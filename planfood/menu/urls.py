from django.urls import path, re_path

from . import views


app_name = "menu"
urlpatterns = [
    re_path(r'api/(?P<uuid>[-\w]+)/$', views.ListMenuDays),
    path('report/', views.create_menu_report_xlsx, name='report'),
]
