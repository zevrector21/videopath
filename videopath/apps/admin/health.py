from django.conf import settings

from videopath.apps.common.services import service_provider


def check_access_to_dumps_bucket():
	service = service_provider.get_service("s3")
	return service.check_access_to_bucket(settings.AWS_DB_DUMPS_BUCKET)

# def check_most_recent_backup():
# 	return "No access"