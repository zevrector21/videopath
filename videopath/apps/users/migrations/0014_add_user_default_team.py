# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_default_teams_to_user(apps, schema_editor):
	User = apps.get_model('users', 'User')
	Team = apps.get_model('users', 'Team')

	for user in User.objects.all():
		if not hasattr(user, 'default_team'):
			Team.objects.create(owner=user, is_default_team_of_user=user, name='My Projects')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20151203_1617'),
    ]

    operations = [
    	 migrations.RunPython(add_default_teams_to_user)
    ]
