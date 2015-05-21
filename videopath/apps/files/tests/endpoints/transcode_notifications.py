

# {
#   "state" : "PROGRESSING",
#   "version" : "2012-09-25",
#   "jobId" : "1432216948982-5kxrlp",
#   "pipelineId" : "1390575655454-1rom96",
#   "input" : {
#     "key" : "some key"
#   },
#   "outputs" : [ {
#     "id" : "1",
#     "presetId" : "1398243331674-sh9v39",
#     "key" : "some key.mp4",
#     "thumbnailPattern" : "some key/{count}-hd",
#     "rotate" : "auto",
#     "status" : "Progressing"
#   } ]
# }

from videopath.apps.common.test_utils import BaseTestCase

from videopath.apps.videos.models import Video
from videopath.apps.files.models import VideoSource

COMPLETE_URL = '/v1/notifications/transcode/complete/'
ERROR_URL = '/v1/notifications/transcode/error/'
PROGRESSING_URL = '/v1/notifications/transcode/progressing/'

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def test_youtube_import(self):

    	# todo 

        # create user and video
        # self.setup_users_and_clients()
        # v=Video.objects.create(user=self.user)

        # response = self.client_user1.post(IMPORT_URL.format(v.pk), {'url':'https://www.youtube.com/watch?v=PPN3KTtrnZM'})
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(VideoSource.objects.first().service, "youtube")
        pass