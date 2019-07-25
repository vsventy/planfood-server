from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.utils import timezone

User = get_user_model()


def get_all_logged_in_users():
    # Query all non-expired sessions
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)


def get_all_active_sessions():
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    data_list = []

    for sessions in sessions:
        data = sessions.get_decoded()
        data_list.append(data)

    return data_list
