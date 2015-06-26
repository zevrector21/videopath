# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20150618_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='currency',
            field=models.CharField(default=b'EUR', max_length=3, choices=[(b'USD', b'US Dollars'), (b'EUR', b'Euro'), (b'GBP', b'British Pounds')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='currency',
            field=models.CharField(default=b'EUR', max_length=3, choices=[(b'USD', b'US Dollars'), (b'EUR', b'Euro'), (b'GBP', b'British Pounds')]),
            preserve_default=True,
        ),
    ]
