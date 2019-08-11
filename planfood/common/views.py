from celery import current_app

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.views.static import serve


class TaskView(View):
    def get(self, request, task_id):
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}

        if task.status == 'SUCCESS':
            response_data['results'] = task.get()

        return JsonResponse(response_data)


@login_required()
def serve_protected_document(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)
