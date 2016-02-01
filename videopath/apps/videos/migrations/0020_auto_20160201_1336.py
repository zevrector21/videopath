# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0019_auto_20151204_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='sprite_length',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='source',
            name='sprite_support',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
