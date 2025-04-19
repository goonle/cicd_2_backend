from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Only authenticated users can read or write
    - Only the blog author can update/delete
    """

    def has_permission(self, request, view):
        # Require authentication for all requests
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Still require authentication for read
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # Allow update/delete only if the user is the blog's author
        return obj.author == request.user
