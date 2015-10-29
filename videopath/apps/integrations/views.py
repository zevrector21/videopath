from rest_framework import viewsets
from rest_framework.response import Response

from .services import config
from .models import Integration

#
# get object description of integration for one user
#
def get_integration_info(user, service):

    # get config of this service
    service_config = config.get(service, None)
    if not service_config:
        return {}

    # see if this config has been enabled
    try:
        integration = Integration.objects.get(user=user, service=service)
    except Integration.DoesNotExist:
        integration = None

    result = {
        'configured': False,
        'id': service,
        'title': service_config.get('title'),
        'oauth2_endpoint': service_config['module'].oauth2_endpoint_for_user(user)
    }

    if integration:
        result['configured'] = True
        result['created'] = integration.created

    return result

#
# get list of integration infos for one user
#
def get_integration_list(user):
    results = []

    for service in config:
        results.append(get_integration_info(user, service))

    return {
        'count': len(results),
        'results': results,
        'next': None,
        'previous': None
    }


#
# Manage the integrations for a user
#
class IntegrationViewSet(viewsets.ViewSet):

    def list(self, request):
        data = get_integration_list(request.user)
        return Response(data)

    # create is disabled
    def create(self, request):
        return Response({}, 404)

    #
    def retrieve(self, request, pk=None):
        data = get_integration_info(request.user, pk)
        return Response(data)

    def update(self, request, pk=None):
        return self.retrieve(request, pk)

    def partial_update(self, request, pk=None):
        return self.retrieve(request, pk)

    #
    # delete data associated with this users integration
    #
    def destroy(self, request, pk=None):
        try:
            integration = Integration.objects.get(user=request.user, service=pk)
            integration.delete()
        except Integration.DoesNotExist:
            pass
        data = get_integration_info(request.user, pk)
        return Response(data)

