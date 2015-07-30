# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_videorevision_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playerappearance',
            old_name='icon',
            new_name='ui_icon',
        ),
        migrations.RenameField(
            model_name='playerappearance',
            old_name='icon_link_target',
            new_name='ui_icon_link_target',
        ),
        migrations.RenameField(
            model_name='playerappearance',
            old_name='language',
            new_name='ui_language',
        ),
        migrations.RemoveField(
            model_name='playerappearance',
            name='sharing_disabled',
        ),
    ]
