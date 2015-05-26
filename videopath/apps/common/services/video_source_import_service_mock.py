

def import_video_from_url( url):

	if "youtube" in url:
		return {'service': 'youtube', 'title': 'Monty Python - Cheese Shop', 'video_aspect': 1.3333333333333333, 'thumbnail_url': 'https://i.ytimg.com/vi/PPN3KTtrnZM/hqdefault.jpg', 'video_duration': 329, 'service_identifier': 'PPN3KTtrnZM'}

	if "wistia" in url:
		return {'service': 'wistia', 'title': u'm35T1YU0KHQ8ZEr28fKgM4sS0zfEOQW3', 'video_aspect': 1.6901408450704225, 'thumbnail_url': u'https://embed-ssl.wistia.com/deliveries/3c2a7d8c8eae310da1862e3e280704b61ae2b4f7.jpg?image_crop_resized=960x540', 'video_duration': 116.259, 'service_identifier': '1gaiqzxu03'}

	if "vimeo" in url:
		return {'service': 'vimeo', 'title': 'Bret Victor - Inventing on Principle', 'video_aspect': 1.7777777777777777, 'thumbnail_url': 'http://i.vimeocdn.com/video/251172173_640.jpg', 'video_duration': 3260, 'service_identifier': '36579366'}

def import_video_from_server(vars):
	return {
			"service":"custom"
		}