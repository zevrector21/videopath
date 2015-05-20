# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosource',
            name='video',
            field=models.ForeignKey(related_name='video_sources', blank=True, to='videos.Video', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videofile',
            name='video',
            field=models.ForeignKey(related_name='file', to='videos.Video'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagefile',
            name='markercontent',
            field=models.ManyToManyField(related_name='image_file', to='videos.MarkerContent', blank=True),
            preserve_default=True,
        ),
    ]
