# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20151204_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
