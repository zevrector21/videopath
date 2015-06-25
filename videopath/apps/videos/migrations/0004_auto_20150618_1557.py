# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20150602_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='videorevision',
            name='password',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videorevision',
            name='password_hashed',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='videorevision',
            name='password_salt',
            field=models.CharField(max_length=512, blank=True),
            preserve_default=True,
        ),
    ]
