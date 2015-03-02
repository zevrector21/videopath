from videopath.apps.common.services import service_provider

def check_stripe_access():
	mail_service = service_provider.get_service("mail")
	return False

def check_transcoder_access():
	service = service_provider.get_service("elastic_transcoder")
	return service.check_connection()

def check_s3_access():
	s3_service = service_provider.get_service("s3")
	return s3_service.check_access()

def check_mandrill_access():
	mail_service = service_provider.get_service("mail")
	return mail_service.check_access()
