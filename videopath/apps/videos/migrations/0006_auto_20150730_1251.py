# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_playerappearance_icon_link_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='nice_name',
        ),
        migrations.RemoveField(
            model_name='videorevision',
            name='video_appearance',
        ),
        migrations.AlterField(
            model_name='video',
            name='player_version',
            field=models.CharField(default=b'3', max_length=20, choices=[(b'1', b'1 - Scruffy'), (b'2', b'2 - Bender'), (b'3', b'3 - Zoidberg'), (b'4', b'4 - Zap Brannigan')]),
            preserve_default=True,
        ),
    ]
