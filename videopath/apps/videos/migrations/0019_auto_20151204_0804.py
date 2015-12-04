# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0018_add_default_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='user',
        ),
        migrations.AlterField(
            model_name='video',
            name='team',
            field=models.ForeignKey(related_name='videos', default=-1, to='users.Team'),
            preserve_default=False,
        ),
    ]
