from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.request import Request
from users.models import User


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view: APIView):
        return request.method in SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_superuser
        )


class IsUserOwner(BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj):
        return obj == request.user or request.user.is_superuser
