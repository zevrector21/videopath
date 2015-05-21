import json

from django.test import Client

from videopath.apps.common.test_utils import BaseTestCase

from videopath.apps.videos.models import Video
from videopath.apps.files.models import VideoFile

COMPLETE_URL = '/v1/notifications/transcode/complete/'
ERROR_URL = '/v1/notifications/transcode/error/'
PROGRESSING_URL = '/v1/notifications/transcode/progressing/'

FILE_KEY = "XXXXXUQJhBfqRITDCgXNBLbLO6j2zmkG"

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

	def setup(self):
		self.setup_users()
		v = Video.objects.create(user=self.user)
		VideoFile.objects.create(video=v, key = FILE_KEY)

		self.dj_client = Client()


	def test_progressing_notification(self):
		return
		data = {
			"Type":"something",
			"Message": json.dumps(progress_notification)
		}
		self.dj_client.post(PROGRESSING_URL, json.dumps(data))
		self.assertEqual(VideoFile.objects.first().status, VideoFile.TRANSCODING_STARTED)

	def test_fail_notification(self):
		return
		data = {
			"Type":"something",
			"Message": json.dumps(failed_notification)
		}
		self.dj_client.post(PROGRESSING_URL, json.dumps(data))
		self.assertEqual(VideoFile.objects.first().status, VideoFile.TRANSCODING_ERROR)

	def test_success_notification(self):
		return
		data = {
			"Type":"something",
			"Message": json.dumps(completed_notification)
		}
		self.dj_client.post(PROGRESSING_URL, json.dumps(data))
		self.assertEqual(VideoFile.objects.first().status, VideoFile.TRANSCODING_COMPLETE)


#
# Test Data
#
progress_notification = {
  "state" : "PROGRESSING",
  "version" : "2012-09-25",
  "jobId" : "1432221152421-7eunhz",
  "pipelineId" : "1390575655454-1rom96",
  "input" : {
    "key" : FILE_KEY,
    "frameRate" : "auto",
    "resolution" : "auto",
    "aspectRatio" : "auto",
    "interlaced" : "auto",
    "container" : "auto"
  },
  "outputs" : [ {
    "id" : "1",
    "presetId" : "1398243331674-sh9v39",
    "key" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG.mp4",
    "thumbnailPattern" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG/{count}-hd",
    "rotate" : "auto",
    "status" : "Progressing"
  }, {
    "id" : "2",
    "presetId" : "1398243385927-5cnjjx",
    "key" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG.webm",
    "thumbnailPattern" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG/{count}",
    "rotate" : "auto",
    "status" : "Progressing"
  } ]
}

completed_notification = {
  "state" : "COMPLETED",
  "version" : "2012-09-25",
  "jobId" : "1432221152421-7eunhz",
  "pipelineId" : "1390575655454-1rom96",
  "input" : {
    "key" : FILE_KEY,
    "frameRate" : "auto",
    "resolution" : "auto",
    "aspectRatio" : "auto",
    "interlaced" : "auto",
    "container" : "auto"
  },
  "outputs" : [ {
    "id" : "1",
    "presetId" : "1398243331674-sh9v39",
    "key" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG.mp4",
    "thumbnailPattern" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG/{count}-hd",
    "rotate" : "auto",
    "status" : "Complete",
    "statusDetail" : "The starting time plus the duration of a clip exceeded the length of the input file. Amazon Elastic Transcoder created an output file that is shorter than the specified duration.",
    "duration" : 90,
    "width" : 1280,
    "height" : 720
  }, {
    "id" : "2",
    "presetId" : "1398243385927-5cnjjx",
    "key" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG.webm",
    "thumbnailPattern" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG/{count}",
    "rotate" : "auto",
    "status" : "Complete",
    "statusDetail" : "The starting time plus the duration of a clip exceeded the length of the input file. Amazon Elastic Transcoder created an output file that is shorter than the specified duration.",
    "duration" : 90,
    "width" : 1280,
    "height" : 720
  } ]
}

failed_notification = {
  "state" : "ERROR",
  "errorCode" : 3001,
  "messageDetails" : "3001 832090b4-c285-4e4f-ad9f-4d287ed5c784: The specified object does not exist in the specified S3 bucket: bucket=vp-video-in, key=some key.",
  "version" : "2012-09-25",
  "jobId" : "1432217012218-qpa0jk",
  "pipelineId" : "1390575655454-1rom96",
  "input" : {
    "key" : FILE_KEY,
    "frameRate" : "auto",
    "resolution" : "auto",
    "aspectRatio" : "auto",
    "interlaced" : "auto",
    "container" : "auto"
  },
  "outputs" : [ {
    "id" : "1",
    "presetId" : "1398243331674-sh9v39",
    "key" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG.mp4",
    "thumbnailPattern" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG/{count}-hd",
    "rotate" : "auto",
    "status" : "Complete",
    "statusDetail" : "The starting time plus the duration of a clip exceeded the length of the input file. Amazon Elastic Transcoder created an output file that is shorter than the specified duration.",
    "duration" : 90,
    "width" : 1280,
    "height" : 720
  }, {
    "id" : "2",
    "presetId" : "1398243385927-5cnjjx",
    "key" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG.webm",
    "thumbnailPattern" : "qmJmXUQJhBfqRITDCgXNBLbLO6j2zmkG/{count}",
    "rotate" : "auto",
    "status" : "Complete",
    "statusDetail" : "The starting time plus the duration of a clip exceeded the length of the input file. Amazon Elastic Transcoder created an output file that is shorter than the specified duration.",
    "duration" : 90,
    "width" : 1280,
    "height" : 720
  } ]
}
