# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integration',
            name='service',
            field=models.CharField(default=b'', max_length=255, choices=[(b'mailchimp', b'mailchimp'), (b'vimeo', b'vimeo'), (b'brightcove', b'brightcove')]),
            preserve_default=True,
        ),
    ]
