# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_usersettings_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automatedmail',
            name='mailtype',
            field=models.CharField(default=b'', max_length=20, choices=[(b'welcome', b'welcome'), (b'follow_up_21', b'follow_up_21'), (b'follow_up_42', b'follow_up_42')]),
            preserve_default=True,
        ),
    ]
