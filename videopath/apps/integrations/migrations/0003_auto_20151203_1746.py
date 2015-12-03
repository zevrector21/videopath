# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20151203_1746'),
        ('integrations', '0002_auto_20151203_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='integration',
            name='team',
            field=models.ForeignKey(related_name='integrations', to='users.Team', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='integration',
            name='user',
            field=models.ForeignKey(related_name='integrations', to='users.User'),
            preserve_default=True,
        ),
    ]
