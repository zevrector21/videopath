# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_videosourcenew'),
        ('videos', '0007_auto_20150730_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='videorevision',
            name='source',
            field=models.ForeignKey(related_name='video_revisions', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='files.VideoSourceNew', null=True),
            preserve_default=True,
        ),
    ]
