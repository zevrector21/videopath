# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='payment_provider',
            field=models.CharField(default=b'stripe', max_length=150, choices=[(b'other', b'other'), (b'stripe', b'stripe'), (b'transfer', b'transfer')]),
            preserve_default=True,
        ),
    ]
