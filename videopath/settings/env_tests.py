#
# Some optimizations for the tests
#
SOUTH_TESTS_MIGRATE = False
DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

#
# Nose
#
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
NOSE_ARGS = [
	'--nocapture'
    # '--with-coverage',
    # '--cover-package=videos',
]

#
# override throttle settings for testing
#
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {
        'anon': '100/second'
}

#
# Load mock services
#
SERVICE_MOCKS = True
