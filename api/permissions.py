from rest_framework.permissions import BasePermission, SAFE_METHODS
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


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission to allow unrestricted access for safe methods,
    but restrict others to authenticated users.
    """
    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS requests for everyone
        if request.method in SAFE_METHODS:
            return True
        # Restrict other methods to authenticated users
        return request.user and request.user.is_authenticated



class IsAdmin(BasePermission):
    """
    Custom permission to grant access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    

class IsReviewOwner(BasePermission):
    """
    Custom permission to grant access only to the owner of the review.
    """
    def has_object_permission(self, request, view, obj):
        # Ensure the object has a `user` attribute (linked to a User)
        return obj.user == request.user
