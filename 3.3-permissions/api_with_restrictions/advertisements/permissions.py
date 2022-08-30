from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' or request.method == 'HEAD':
            return True
        return request.user == obj.user