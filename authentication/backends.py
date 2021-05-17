from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from app.models import Student, Teacher


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

        return None


def is_user_has_profile(obj):
    if Student.objects.filter(user=obj) or Teacher.objects.filter(user=obj):
        return True
    else:
        return False
    