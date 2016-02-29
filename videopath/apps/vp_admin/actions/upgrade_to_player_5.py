

def run(video):
	if video.player_version == 5:
		return 'Video already upgraded.'

	video.player_version = 5
	video.save()

	video.current_revision.source.sprite_support = False
	video.current_revision.source.save()
	video.current_revision.source.export_jpg_sequence()

	return 'Upgrading...'
