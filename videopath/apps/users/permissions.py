from rest_framework import permissions

class UserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):

    	if request.user != obj:
    		return False

    	# require password when changing (putting) the object
    	if request.method in ["PUT", "PATCH"]:
    		password = request.data.get("password", None)
    		return request.user.check_password(password)

    	# safe methods are ok, as we've already made sure
    	# that the user may get this
        if request.method in permissions.SAFE_METHODS:
            return True

        return False

class TeamPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False

class TeamMemberPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False