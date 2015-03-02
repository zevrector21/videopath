import os

from boto.s3.connection import S3Connection

from django.conf import settings

connection = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)

# 
# Upload a file or a string to s3
#
def upload(source, bucket, key, content_type = None, cache_control = None, verify = False, public = False):
	
	# get key
	bucket = connection.get_bucket(bucket)
	key = bucket.new_key(key)

	# set metadata
	if content_type:
		key.set_metadata("Content-Type", content_type)
	if cache_control:
		key.set_metadata("Cache-Control", cache_control)

	# define access policy
	policy = "public-read" if public else "private"

	# define wether to upload from file or from string
	if isinstance(source, basestring):

		# upload from fiel path
		if os.path.exists(source):
			 key.set_contents_from_filename(source)

		# upload from string
		else:
			key.set_contents_from_string(source, policy=policy)

	# upload from file object
	else:
		pass

	if verify:
		# verify upload
		pass

	return True

#
# Delete a key
#
def delete(bucket, key):
    bucket = connection.get_bucket(bucket)
    bucket.delete_key(key)
    return True

#
# List all keys in a bucket
#
def list_keys(bucket, prefix = ""):
	bucket = connection.get_bucket(bucket)
	return bucket.list(prefix=prefix)

#
# Check existence of a key
#
def check_existence(bucket, key):
	bucket = connection.get_bucket(settings.AWS_UPLOAD_BUCKET)
	key = bucket.get_key(key)
	return key != None

#
#
#
def check_access():
	try:
		connection.get_all_buckets()
		return True
	except Exception as e:
		return str(e)

#
# Check if we have full access to a certain bucket
#
def check_access_to_bucket(bucket):
	try:
		upload("test", bucket, "test_key")
		delete(bucket, "test_key")
		return True
	except Exception as e:
		return str(e)