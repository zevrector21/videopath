from PIL import Image, ImageOps
import string, random

default_conf = {
	"operation": "fit",
	"size": (100, 100)
}

def resize_image_file(f, conf = {}):

	_conf = default_conf.copy()
	_conf.update(conf)

	# persist file
	tmp_name_in = "/tmp/" + _random_string()
	tmp_name_out = "/tmp/" + _random_string()
	with open(tmp_name_in, 'wb+') as destination:
		for chunk in f.chunks():
		    destination.write(chunk)

	# convert image
	has_transparency = False
	image = Image.open(tmp_name_in)
	if image.mode == "RGBA" or image.mode == "transparency":
	    has_transparency = True
	image = image.convert("RGBA")

	if _conf["operation"] is "fit":
		image = ImageOps.fit(image, _conf["size"])

	# save back to disk
	image.save(tmp_name_out, "PNG" if has_transparency else "JPEG", quality=90)

	return tmp_name_out


def _random_string():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))