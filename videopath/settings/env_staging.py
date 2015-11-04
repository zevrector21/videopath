
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


#
# Set dev player locations
#
AWS_PLAYER_BUCKET = "player-dev.videopath.com"
PLAYER_SRC = '//player-dev.videopath.com/develop/'
PLAYER_LOCATION = 'http://player-dev.videopath.com/'

#
# Endpoint for JPG engine streaming
#
JPGS_CDN = '//videopathmobilefilesdev.blob.core.windows.net/'

#
# Integrations
#

#
# Endpoint
#
API_ENDPOINT = 'https://videopath-api-dev.herokuapp.com'

APP_URL = 'https://app-dev.videopath.com/develop'
