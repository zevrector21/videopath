# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videorevision_continuous_playback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='player_version',
            field=models.CharField(default=b'3', max_length=20, choices=[(b'1', b'1 - Scruffy'), (b'2', b'2 - Bender'), (b'3', b'3 - Zoidberg')]),
            preserve_default=True,
        ),
    ]
