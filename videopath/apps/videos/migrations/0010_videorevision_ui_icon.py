# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_auto_20150812_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='videorevision',
            name='ui_icon',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
    ]
