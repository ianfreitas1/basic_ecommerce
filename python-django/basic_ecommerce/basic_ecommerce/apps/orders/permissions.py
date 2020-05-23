from rest_framework.permissions import BasePermission


class ObjectPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
