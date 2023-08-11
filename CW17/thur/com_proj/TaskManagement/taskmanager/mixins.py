from .models import Task
from django.core.exceptions import PermissionDenied


class TodoOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        todo = Task.objects.get(id=kwargs['pk'])
        if not todo.author == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ObjectGetUpdateMixin:
    RelatedField = None

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj.get_attr(self.RelatedField) == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        object_pk = self.kwargs.get('pk')
        obj = self.model_class(pk=object_pk)
        return obj

    def update_object(self):
        form = self.form_class(self.request.POST, instance=self.get_object())
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return obj
