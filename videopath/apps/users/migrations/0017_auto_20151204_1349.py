# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20151204_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='is_default_team_of_user',
            field=models.OneToOneField(related_name='default_team', null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name=b'default_team_of_user'),
            preserve_default=True,
        ),
    ]
