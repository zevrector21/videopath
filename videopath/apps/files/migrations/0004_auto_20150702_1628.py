# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_videosource_allow_youtube_clickthrough'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosource',
            name='service',
            field=models.CharField(default=b'none', max_length=255, choices=[(b'none', b'none'), (b'youtube', b'youtube'), (b'vimeo', b'vimeo'), (b'wistia', b'wistia'), (b'brightcove', b'brightcove'), (b'custom', b'custom')]),
            preserve_default=True,
        ),
    ]
