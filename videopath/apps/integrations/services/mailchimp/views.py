from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import mailchimp

from videopath.apps.integrations.decorators import authenticate_service_viewset

#
# Send list of available lists to user
#
class ListsViewSet(viewsets.ViewSet):
	@authenticate_service_viewset('mailchimp')
	def list(self, request, credentials):
		print credentials
		mc = mailchimp.Mailchimp(credentials['api_key'])
		result = mc.lists.list()

		results = map(lambda item: {'id': item['id'], 'name': item['name']}, result['data'] )

		return Response({
			'count': len(results),
	        'results': results,
	        'next': None,
	        'previous': None
			})

#
# beacon endpoint
#
@api_view(['GET'])
@permission_classes((AllowAny,))
def beacon(request):
	return Response()


