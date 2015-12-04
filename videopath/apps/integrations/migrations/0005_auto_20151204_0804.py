# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0004_add_default_teams'),
        ('users', '0015_auto_20151203_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integration',
            name='team',
            field=models.ForeignKey(related_name='integrations', default=-1, to='users.Team'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='integration',
            unique_together=set([('team', 'service')]),
        ),
        migrations.RemoveField(
            model_name='integration',
            name='user',
        ),
    ]
