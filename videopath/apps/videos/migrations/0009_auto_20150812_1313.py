# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_videorevision_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='videorevision',
            name='tracking_pixel_end',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videorevision',
            name='tracking_pixel_q1',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videorevision',
            name='tracking_pixel_q2',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videorevision',
            name='tracking_pixel_q3',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videorevision',
            name='tracking_pixel_start',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='player_version',
            field=models.CharField(default=b'4', max_length=20, choices=[(b'1', b'1 - Scruffy'), (b'2', b'2 - Bender'), (b'3', b'3 - Zoidberg'), (b'4', b'4 - Zap Brannigan')]),
            preserve_default=True,
        ),
    ]
