# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(unique=True, max_length=50, blank=True)),
                ('status', models.SmallIntegerField(default=0, choices=[(0, b'Created. Waiting for upload.'), (1, b'Uploaded.'), (2, b'Processing'), (3, b'Processed.'), (-1, b'Error.')])),
                ('image_type', models.CharField(default=b'marker content', max_length=255, blank=True, choices=[(b'marker content', b'Image for Marker Content'), (b'custom thumbnail', b'Image for custom video thumbnail'), (b'custom logo', b'Image for custom logo on player chrome')])),
                ('width', models.SmallIntegerField(default=0)),
                ('height', models.SmallIntegerField(default=0)),
                ('bytes', models.BigIntegerField(default=0)),
                ('original_file_name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(unique=True, max_length=50, blank=True)),
                ('status', models.SmallIntegerField(default=0, choices=[(0, b'Created. Waiting for upload.'), (1, b'Uploaded.'), (2, b'Transcoding job submitted.'), (3, b'Transcoding started.'), (4, b'Transcoding complete.'), (-1, b'Transcoding error.')])),
                ('transcoding_job_id', models.CharField(max_length=255, blank=True)),
                ('transcoding_result', models.CharField(max_length=255, blank=True)),
                ('video_width', models.SmallIntegerField(default=0)),
                ('video_height', models.SmallIntegerField(default=0)),
                ('video_duration', models.FloatField(default=0)),
                ('video_aspect', models.FloatField(default=0)),
                ('thumbnail_index', models.SmallIntegerField(default=0)),
                ('original_file_name', models.CharField(max_length=255, blank=True)),
                ('original_bytes', models.BigIntegerField(default=0)),
                ('transcoded_bytes', models.BigIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('service', models.CharField(default=b'none', max_length=255, choices=[(b'none', b'none'), (b'youtube', b'youtube'), (b'vimeo', b'vimeo'), (b'wistia', b'wistia'), (b'custom', b'custom')])),
                ('status', models.SmallIntegerField(default=0, choices=[(0, b'created'), (1, b'ok'), (-1, b'error')])),
                ('service_identifier', models.CharField(default=b'', max_length=255)),
                ('source_mp4', models.CharField(default=b'', max_length=512, blank=True)),
                ('source_webm', models.CharField(default=b'', max_length=512, blank=True)),
                ('video_duration', models.FloatField(default=0)),
                ('video_aspect', models.FloatField(default=0)),
                ('title', models.CharField(default=b'', max_length=255)),
                ('thumbnail_url', models.CharField(default=b'', max_length=2048)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
