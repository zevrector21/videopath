
#
# Set staging var to true
#
STAGING = True

#
# Set Heroku DB
#
import dj_database_url
if dj_database_url.config():
    DATABASES['default'] = dj_database_url.config()