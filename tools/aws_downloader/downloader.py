from boto.s3.connection import S3Connection
import os


connection = S3Connection("", '')
bucket = connection.get_bucket("jpgs.videopath.com")

for key in bucket.list():
	print key.name
	filename = os.path.dirname(os.path.abspath(__file__))+"/"+key.name
	dirname = os.path.dirname(filename)
	try:
		os.makedirs(dirname)
	except:
		pass
	try:
		key.get_contents_to_filename(filename)
	except:
		pass

