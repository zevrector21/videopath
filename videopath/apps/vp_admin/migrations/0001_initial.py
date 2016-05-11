# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0015_auto_20160511_1515'),
        ('videos', '0024_auto_20160511_1515'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('payments.payment',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('videos.video',),
        ),
    ]
