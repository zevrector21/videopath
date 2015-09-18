# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_auto_20150626_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCampaignData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('source', models.CharField(max_length=512)),
                ('medium', models.CharField(max_length=512)),
                ('name', models.CharField(max_length=512)),
                ('content', models.CharField(max_length=512)),
                ('term', models.CharField(max_length=512)),
                ('user', models.OneToOneField(related_name='campaign_data', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
