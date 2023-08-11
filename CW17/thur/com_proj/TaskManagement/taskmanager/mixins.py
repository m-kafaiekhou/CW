from .models import Task
from django.core.exceptions import PermissionDenied


class TodoOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        todo = Task.objects.get(id=kwargs['pk'])
        if not todo.author == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

