# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalanalyticsdata',
            name='video',
            field=models.ForeignKey(related_name='total_analytics', to='videos.Video'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dailyanalyticsdata',
            name='video',
            field=models.ForeignKey(related_name='daily_analytics', to='videos.Video'),
            preserve_default=True,
        ),
    ]
