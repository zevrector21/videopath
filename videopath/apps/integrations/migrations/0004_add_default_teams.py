# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_default_teams_to_integrations(apps, schema_editor):
	Integrations = apps.get_model('integrations', 'Integration')
	for i in Integrations.objects.all():
		i.team = i.user.default_team
		i.save()

class Migration(migrations.Migration):

    dependencies = [
    	('users', '0015_auto_20151203_1746'),
        ('integrations', '0003_auto_20151203_1746'),
    ]

    operations = [
    	migrations.RunPython(add_default_teams_to_integrations)
    ]
