from django.urls import path

from . import views


urlpatterns = [path('api/(?P<uuid>[-\w]+)/$', views.ListMenuDays)]
