# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20150702_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSourceNew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('service', models.CharField(default=b'none', max_length=255, choices=[(b'none', b'none'), (b'youtube', b'youtube'), (b'vimeo', b'vimeo'), (b'wistia', b'wistia'), (b'brightcove', b'brightcove'), (b'videopath', b'videopath'), (b'custom', b'custom')])),
                ('status', models.CharField(default=b'created', max_length=255, choices=[(b'created', b'created'), (b'file received', b'file received'), (b'file received', b'file received'), (b'ok', b'ok'), (b'error', b'error')])),
                ('service_identifier', models.CharField(default=b'', max_length=255)),
                ('duration', models.FloatField(default=0)),
                ('aspect', models.FloatField(default=0)),
                ('width', models.SmallIntegerField(default=0)),
                ('height', models.SmallIntegerField(default=0)),
                ('description', models.CharField(default=b'', max_length=255)),
                ('thumbnail_small', models.CharField(default=b'', max_length=2048)),
                ('thumbnail_large', models.CharField(default=b'', max_length=2048)),
                ('source_mp4', models.CharField(default=b'', max_length=512, blank=True)),
                ('source_webm', models.CharField(default=b'', max_length=512, blank=True)),
                ('youtube_allow_clickthrough', models.BooleanField(default=False)),
                ('videopath_transcoding_job_id', models.CharField(max_length=255, blank=True)),
                ('videopath_transcoding_result', models.CharField(max_length=255, blank=True)),
                ('iphone_enabled', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
