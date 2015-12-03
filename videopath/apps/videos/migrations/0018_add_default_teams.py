# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_default_teams_to_videos(apps, schema_editor):
	Video = apps.get_model('videos', 'Video')
	for v in Video.objects.all():
		v.team = v.user.default_team
		v.save()

class Migration(migrations.Migration):

    dependencies = [
    	('users', '0015_auto_20151203_1746'),
        ('videos', '0017_auto_20151203_1746'),
    ]

    operations = [
    	migrations.RunPython(add_default_teams_to_videos)
    ]
