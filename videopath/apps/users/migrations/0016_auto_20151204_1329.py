# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20151203_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammember',
            old_name='member_type',
            new_name='role',
        ),
    ]
