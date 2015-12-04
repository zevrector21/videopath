from rest_framework import permissions


class AuthenticatedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()

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
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and obj.is_user_member(request.user):
            return True
        if request.method == "DELETE" and obj.is_user_owner(request.user) and obj.can_be_deleted():
            return True
        if request.method in ["PUT", "PATCH"] and obj.is_user_admin(request.user):
            return True
        return False

class TeamMemberPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: return True

    def has_object_permission(self, request, view, obj):
        team = obj.team

        # admins of teams can add and remove users
        if team.is_user_admin(request.user): 
            return True

        # members of teams can see other members
        if request.method in permissions.SAFE_METHODS and team.is_user_member:
            return True

        return False