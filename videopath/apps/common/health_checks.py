import importlib

from django.conf import settings


def run():
	failed = 0
	succeeded = 0
	apps = {}
	installed_apps = settings.INSTALLED_APPS + ('videopath.apps.common',)

	for app in installed_apps:
		try:
			health_module = app + ".health"
			module = importlib.import_module(health_module)
			result, s, f = _run_module_test(module)
			apps[app] = result
			succeeded += s
			failed += f
		except ImportError:
			pass


	return {
		"failed": failed,
		"succeeded": succeeded,
		"apps": apps
	}

def _run_module_test(module):
	result = {}
	failed = 0
	succeeded = 0
	for func in dir(module): 
		if "check_" in func:
			function = getattr(module, func)
			check_result = function()
			name = func.replace("check_", "").replace("_", " ")

			if check_result == True:
				result[name] = "OK"
				succeeded+=1
			else:
				result[name] = "FAILED - " + str(check_result)
				failed+=1
	return result, succeeded, failed
