from django.core.paginator import Paginator

from rest_framework import pagination

#
#  Helper to get a paginated output of otherwise flat serilizer output
#
def get_paginated_serializer(objects, serializer_class, page_size=20, page=1):
	page =  Paginator(objects, page_size).page(page)
	class SerializerClass(pagination.PaginationSerializer):
	        class Meta:
	            object_serializer_class = serializer_class
	return SerializerClass(page)