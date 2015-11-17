# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_usersalesinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='phone_number',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
