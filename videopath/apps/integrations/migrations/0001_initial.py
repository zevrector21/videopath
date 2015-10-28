# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Integration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('service', models.CharField(default=b'', max_length=255, choices=[(b'mailchimp', b'mailchimp')])),
                ('credentials', models.CharField(max_length=2048, blank=True)),
                ('settings', models.CharField(max_length=2048, blank=True)),
                ('user', models.ForeignKey(related_name='integrations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='integration',
            unique_together=set([('user', 'service')]),
        ),
    ]
