from .models import Task
from django.core.exceptions import PermissionDenied


class TodoOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        todo = Task.objects.get(id=kwargs['pk'])
        if not todo.author == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class ObjectGetUpdateMixin:
    def __init__(self, request, model, check, id):
        self.request = request
        self.model = model
        self.check = check
        self.id = id

    def get_object(self):


    def dispatch(self, request, *args, **kwargs):
        todo = Task.objects.get(id=kwargs['pk'])
        if not todo.author == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)