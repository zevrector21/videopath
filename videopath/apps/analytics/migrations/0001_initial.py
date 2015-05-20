# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAnalyticsData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('sessions', models.IntegerField(default=0)),
                ('plays_all', models.IntegerField(default=0)),
                ('plays_unique', models.IntegerField(default=0)),
                ('overlays_opened_all', models.IntegerField(default=0)),
                ('overlays_opened_unique', models.IntegerField(default=0)),
                ('avg_session_time', models.FloatField(default=0)),
                ('popular_markers', models.TextField(default=b'{}')),
                ('video_completed', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TotalAnalyticsData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('sessions', models.IntegerField(default=0)),
                ('plays_all', models.IntegerField(default=0)),
                ('plays_unique', models.IntegerField(default=0)),
                ('overlays_opened_all', models.IntegerField(default=0)),
                ('overlays_opened_unique', models.IntegerField(default=0)),
                ('avg_session_time', models.FloatField(default=0)),
                ('popular_markers', models.TextField(default=b'{}')),
                ('video_completed', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
