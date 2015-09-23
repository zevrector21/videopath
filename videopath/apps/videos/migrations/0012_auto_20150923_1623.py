# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_auto_20150918_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(unique=True, max_length=50, blank=True)),
                ('status', models.CharField(default=b'ok', max_length=255, choices=[(b'awaiting_upload', b'awaiting_upload'), (b'processing', b'processing'), (b'ok', b'ok'), (b'error', b'error')])),
                ('service_identifier', models.CharField(default=b'', max_length=255)),
                ('service', models.CharField(default=b'none', max_length=255, choices=[(b'none', b'none'), (b'youtube', b'youtube'), (b'vimeo', b'vimeo'), (b'wistia', b'wistia'), (b'brightcove', b'brightcove'), (b'videopath', b'videopath'), (b'custom', b'custom')])),
                ('duration', models.FloatField(default=0)),
                ('aspect', models.FloatField(default=0)),
                ('description', models.CharField(default=b'', max_length=255)),
                ('thumbnail_small', models.CharField(default=b'', max_length=2048)),
                ('thumbnail_large', models.CharField(default=b'', max_length=2048)),
                ('file_mp4', models.CharField(default=b'', max_length=512, blank=True)),
                ('file_webm', models.CharField(default=b'', max_length=512, blank=True)),
                ('youtube_allow_clickthrough', models.BooleanField(default=False)),
                ('notes', models.CharField(max_length=255, blank=True)),
                ('jpg_sequence_support', models.BooleanField(default=False)),
                ('jpg_sequence_length', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='videorevision',
            name='source',
        ),
    ]
