import os

#
# define wether mock versions of services should be loaded
#
SERVICE_MOCKS = False

#
# Setup mem cachify caches
#
from memcacheify import memcacheify
CACHES = memcacheify()

#
# Player config for export
#
PLAYER_DEFAULT_VERSION = '2'
PLAYER_SRC = '//src.videopath.com/player/'
PLAYER_LOCATION = 'http://player.videopath.com/'

#
# CDN Endpoints
#
VIDEO_CDN = '//videos.videopath.com/'
THUMBNAIL_CDN = '//thumbs.videopath.com/'
IMAGE_CDN = 'https://images.videopath.com/'
DOCS_CDN = "http://docs.videopath.com/"

#
# demo videos
#
DEMO_VIDEOS = {
    "1": "2rtGFAnyf-s"
}

#
# Invoice Numbers
#
INVOICE_START_NUMBER = 32049

#
# URL for pg backups on heroku
#
PGBACKUPS_URL = os.environ.get("PGBACKUPS_URL")

#
# Default values for appearance
#
DEFAULT_VIDEO_APPEARANCE = {

	# Language of the interface, notably the "click me" alert.
    "language": "en", 

    # custom colors
    "ui_color_1": None, 
    "ui_color_2": None, 

    # settings
    "sharing_disabled": False, 

    # logos & icons
    "endscreen_logo": None, 
    "icon": None
}

