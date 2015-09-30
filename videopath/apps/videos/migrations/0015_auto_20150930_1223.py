# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_videorevision_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videorevision',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
