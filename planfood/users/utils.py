from django.core.exceptions import PermissionDenied


def check_logged_users_rights(request):
    if request.user.can_logged_users or request.user.is_superuser:
        request.can_logged_users = True
        return request

    raise PermissionDenied
