from videopath.apps.analytics.services import ga_import_service

def check_access_to_google_analytics():
	return ga_import_service.check_access()
