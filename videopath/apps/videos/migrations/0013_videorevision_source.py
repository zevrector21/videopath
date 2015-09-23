# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_auto_20150923_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='videorevision',
            name='source',
            field=models.ForeignKey(related_name='revisions', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='videos.Source', null=True),
            preserve_default=True,
        ),
    ]
