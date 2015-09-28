# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_videosourcenew'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videofile',
            name='video',
        ),
        migrations.DeleteModel(
            name='VideoFile',
        ),
        migrations.RemoveField(
            model_name='videosource',
            name='video',
        ),
        migrations.DeleteModel(
            name='VideoSource',
        ),
        migrations.DeleteModel(
            name='VideoSourceNew',
        ),
    ]
