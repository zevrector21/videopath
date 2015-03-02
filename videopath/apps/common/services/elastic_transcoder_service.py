from boto import elastictranscoder
from boto import sns

from django.conf import settings

AWS_REGION = 'us-west-2'

#
# Start a transcoding job
#
def start_transcoding_job(input, other, outputs):
	transcoder = elastictranscoder.connect_to_region(AWS_REGION)
	job = transcoder.create_job(settings.AWS_PIPELINE_ID, input, other, outputs)

	if job:
		return job['Job']['Id']
	else:
		return False


#
# Confirm SNS subscription
#
def confirm_subscription_topic(topic, token):
	conn = sns.connect_to_region(AWS_REGION)
	return conn.confirm_subscription(topic, token)

#
#
#
def check_connection():
	try:
		# list our pipelines, just to see if the connection to the service
		# works
		t = elastictranscoder.connect_to_region(AWS_REGION)
		t.list_pipelines()
		return True
	except Exception as e:
		return str(e)
