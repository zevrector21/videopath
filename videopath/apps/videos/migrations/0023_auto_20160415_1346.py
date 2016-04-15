# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0022_auto_20160314_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='videorevision',
            name='ui_icon_link_target',
            field=models.CharField(default=b'https://videopath.com', max_length=1024, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='player_version',
            field=models.CharField(default=b'5', max_length=20, choices=[(b'1', b'1 - Scruffy'), (b'2', b'2 - Bender'), (b'3', b'3 - Zoidberg'), (b'4', b'4 - Zap Brannigan'), (b'5', b'5 - Leila'), (b'6', b'6 - Hedonism Bot')]),
        ),
    ]
