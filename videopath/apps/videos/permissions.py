import json

from rest_framework import permissions

from videopath.apps.videos.models import VideoRevision, Marker

class AuthenticatedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()

class VideoRevisionPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        try:
            data = json.loads(request.body)
            revision = VideoRevision.objects.get(pk=data["id"])
            return revision.video.user == request.user
        except Exception:
            return False

    def has_object_permission(self, request, view, obj):
        if obj.video.user == request.user:
            return True
        return False


class MarkerPermissions(permissions.BasePermission):

    # only allow access if the video revision belongs to a users video
    def has_permission(self, request, view):
        if request.method in ["GET", "DELETE"]:
            return True
        try:
            data = json.loads(request.body)
            revision = VideoRevision.objects.get(pk=data["video_revision"])
            return revision.video.user == request.user
        except Exception:
            return False

    def has_object_permission(self, request, view, obj):
        if obj.video_revision.video.user == request.user:
            return True
        return False

class VideoPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user and not obj.archived:
            return True
        return False

class MarkerContentPermissions(permissions.BasePermission):

    # make sure the marker content belongs to a video we have access to
    def has_permission(self, request, view):
        if request.method in ["GET", "DELETE"]:
            return True
        try:
            data = json.loads(request.body)
            marker = Marker.objects.get(pk=data["marker"])
            return marker.video_revision.video.user == request.user
        except Exception:
            return False

    def has_object_permission(self, request, view, obj):
        if obj.marker.video_revision.video.user == request.user:
            return True
        return False
