# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0013_videorevision_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='videorevision',
            name='published_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
