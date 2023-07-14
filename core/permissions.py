from rest_framework.permissions import BasePermission
from core.models import UserRoles


class IsOwner(BasePermission):
    message = 'Доступ ограничен'

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "owner"):
            owner = obj.owner
        elif hasattr(obj, "author"):
            owner = obj.author
        else:
            raise Exception("error")

        if request.user == obj.owner:
            return True
        return False


class IsStaff(BasePermission):
    message = 'Доступ запрещён'

    def has_object_permission(self, request, view, obj):
        if request.user.role in [UserRoles.ADMIN, UserRoles.USER]:
            return True
        return False
