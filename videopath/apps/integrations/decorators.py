import json

from django.shortcuts import get_object_or_404

from .models import Integration

def authenticate_service_view(service):

	def decorator(view):
		def _wrapped_view(request, *args, **kwargs):
			s = get_object_or_404(Integration, user=request.user, service=service)
			return view(request, json.loads(s.credentials), *args, **kwargs)
		return _wrapped_view

	return decorator

def authenticate_service_viewset(service):

	def decorator(view):
		def _wrapped_view(instance, request, *args, **kwargs):
			s = get_object_or_404(Integration, user=request.user, service=service)
			return view(instance, request, json.loads(s.credentials), *args, **kwargs)
		return _wrapped_view

	return decorator
