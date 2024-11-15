from rest_framework import permissions

class AdminOrOwnerOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins or the owner of the object to edit or delete it.
    """
    def has_permission(self, request, view):
        # Allow read-only
        if request.method in permissions.SAFE_METHODS:
            return True
        # For non-safe methods (POST, PUT, DELETE), ensure the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read-only 
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write/delete permissions are only allowed to the owner or admin users
        return request.user.is_staff or obj.owner == request.user
