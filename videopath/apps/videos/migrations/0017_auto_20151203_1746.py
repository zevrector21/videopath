# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20151203_1746'),
        ('videos', '0016_auto_20151130_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='team',
            field=models.ForeignKey(related_name='videos', to='users.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(related_name='videos', to='users.User'),
            preserve_default=True,
        ),
    ]
