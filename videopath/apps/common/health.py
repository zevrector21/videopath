from videopath.apps.common.services import service_provider

def check_stripe_access():
	service = service_provider.get_service("stripe")
	return service.check_access()

def check_transcoder_access():
	service = service_provider.get_service("elastic_transcoder")
	return service.check_connection()

def check_s3_access():
	service = service_provider.get_service("s3")
	return service.check_access()

def check_mandrill_access():
	service = service_provider.get_service("mail")
	return service.check_access()

def check_db_connection():
	try:
		from django.db import connection
		cursor = connection.cursor()
		cursor.execute("select 1")
		return True
	except Exception as e:
		return str(e)