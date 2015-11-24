# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20151123_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='receive_retention_emails',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usersettings',
            name='receive_system_emails',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
