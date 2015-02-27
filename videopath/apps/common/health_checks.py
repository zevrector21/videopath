import importlib

from django.conf import settings


def run():
	failed = 0
	succeeded = 0
	apps = {}

	for app in settings.INSTALLED_APPS:
		try:
			health_module = app + ".health"
			module = importlib.import_module(health_module)
			result = _run_module_test(module)
			apps[app] = result
		except ImportError:
			pass


	return {
		"failed": failed,
		"succeeded": succeeded,
		"apps": apps
	}

def _run_module_test(module):
	result = {}
	for func in dir(module): 
		if "check_" in func:
			function = getattr(module, func)
			check_result = function()
			result[func] = "OK"
	return result
