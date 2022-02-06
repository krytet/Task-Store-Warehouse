from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsWarehouseOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.warehouse or \
               (request.method in SAFE_METHODS)
