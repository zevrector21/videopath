from azure.storage import BlobService
import os

# credentials
blob_service = BlobService(account_name='videopath', account_key='74z/zY+Fo709d6CbbPL6mbrLmE6hHzZsPZPzLA+4S5OzjTUxr8mAW6UhWdG1v8ooiEGx/RBfkz3FZTpPDLi06A==')

# perform upload
def upload_file(source, key):
	fileName, fileExtension = os.path.splitext(source)
	content_type = ''

	if fileExtension == ".mp3":
		content_type = "audio/mpeg"
	elif fileExtension == ".jpg":
		content_type = "image/jpeg"
	elif fileExtension == ".png":
		content_type = "image/png"

	blob_service.put_block_blob_from_path(
	    'jpgs',
	    key,
	    source,
	    x_ms_blob_content_type=content_type,
	    x_ms_blob_cache_control='public, max-age=600'
	)


# walk all files in dir and push to bucket
codepath = os.path.dirname(os.path.abspath(__file__)) + "/upload"
for path, subdirs, files in os.walk(codepath):
    for name in files:
        # don't upload hidden files
        if name[0] == ".":
            continue

        pathname = os.path.join(path, name)
        keyname = pathname.replace(codepath, "")[1:] 

        print pathname + " --> " + keyname

        upload_file(pathname, keyname)
