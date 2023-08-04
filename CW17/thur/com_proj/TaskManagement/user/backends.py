from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(CustomUser.EMAIL_FIELD)
        if username is None or password is None:
            return
        try:
            if '@' in username:
                user = CustomUser.objects.get(username=username)
            else:
                user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            CustomUser().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
    # def authenticate(self, request, username=None, email=None, password=None, **kwargs):
    #     if username is None:
    #         username = kwargs.get(CustomUser.USERNAME_FIELD)
    #     if email is None:
    #         email = kwargs.get(CustomUser.EMAIL_FIELD)
    #     if (username or email) is None or password is None:
    #         return
    #     try:
    #         if username:
    #             user = CustomUser.objects.get(username=username)
    #         elif email:
    #             user = CustomUser.objects.get(email=email)
    #     except CustomUser.DoesNotExist:
    #         # Run the default password hasher once to reduce the timing
    #         # difference between an existing and a nonexistent user (#20760).
    #         CustomUser().set_password(password)
    #     else:
    #         if user.check_password(password) and self.user_can_authenticate(user):
    #             return user
