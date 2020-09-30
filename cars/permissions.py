from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read only permissions
        if request.method in permissions.SAFE_METHODS:
            return True

        # Admin only - Hard coded - Don't do this here
        # return request.user.id == 1

        # Write permissions
        return obj.author == request.user