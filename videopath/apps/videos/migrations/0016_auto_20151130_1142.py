# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import videopath.apps.common.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0015_auto_20150930_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerappearance',
            name='ui_click_hint_appearences',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playerappearance',
            name='ui_click_hint_color',
            field=videopath.apps.common.models.ColorField(default=b'#ffffff', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='markercontent',
            name='type',
            field=models.CharField(default=b'text', max_length=20, choices=[(b'text', b'text'), (b'title', b'title'), (b'image', b'image'), (b'website', b'website'), (b'map', b'map'), (b'video', b'video'), (b'media', b'media'), (b'audio', b'audio'), (b'simple_button', b'simple_button'), (b'social', b'social'), (b'email_collector', b'email_collector')]),
            preserve_default=True,
        ),
    ]
