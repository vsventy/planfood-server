from django.urls import path

from planfood.users.views import (
    user_detail_view,
    user_list_view,
    user_redirect_view,
    user_update_view,
    logged_users_list_view,
)


app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("logged", view=logged_users_list_view, name="logged_list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
