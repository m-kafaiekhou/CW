from .models import CustomUser
from django.core.exceptions import PermissionDenied


class OwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=kwargs['pk'])
        if not user == request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)