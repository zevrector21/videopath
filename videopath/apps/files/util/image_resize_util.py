from boto.s3.connection import S3Connection
from PIL import Image

from django.conf import settings

from videopath.apps.files.settings import image_sizes
from videopath.apps.files.models import ImageFile

def process_image_file(f):

    try:
        # s3 connetion
        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        in_bucket = conn.get_bucket(settings.AWS_UPLOAD_BUCKET)
        out_bucket = conn.get_bucket(settings.AWS_IMAGE_OUT_BUCKET)

        # get config for filetype
        conf = image_sizes[f.image_type]

        # if file is not fresh
        if f.status != ImageFile.FILE_RECEIVED:
            return 
        f.status = ImageFile.PROCESSING
        f.save()

        # try to retrieve image file
        in_key = in_bucket.get_key(f.key)
        if in_key is None or in_key.size > conf["maxSize"]:
            f.status == ImageFile.ERROR
            f.save()
            return

        # define file paths and load from key
        filename = "/tmp/" + f.key
        tempname = "/tmp/" + f.key + ":out"
        in_key.get_contents_to_filename(filename)

        for out in conf["outs"]:

            # convert image
            has_transparency = False
            image = Image.open(filename)
            if image.mode == "RGBA" or image.mode == "transparency":
                has_transparency = True
            image = image.convert("RGBA")

            if out["type"] == "thumbnail":
                image.thumbnail((out["maxWidth"], out["maxHeight"]), Image.ANTIALIAS)

            image.save(tempname, "PNG" if has_transparency else "JPEG")

            # save image back to s3
            key = out["key"].replace("_FILEKEY_", f.key)
            out_key = out_bucket.new_key(key)
            out_key.set_contents_from_filename(tempname, policy="public-read")

            # update file object
            width, height = image.size
            f.width = width
            f.height = height

        f.status = ImageFile.PROCESSED
        f.save()


    # log error
    except:
        f.status == ImageFile.ERROR
        f.save()



