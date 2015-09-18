# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import videopath.apps.common.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_videorevision_ui_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videorevision',
            name='ui_color_1',
            field=videopath.apps.common.models.ColorField(default=b'#273a45', max_length=10),
            preserve_default=True,
        ),
    ]
