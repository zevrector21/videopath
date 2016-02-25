# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0011_auto_20160201_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='email',
            field=models.CharField(default=b'', max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='paymentdetails',
            name='notes',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
    ]
