# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import videopath.apps.common.models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(db_index=True, max_length=50, blank=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('time', models.FloatField(default=0)),
                ('overlay_width', models.IntegerField(default=-1)),
                ('overlay_height', models.IntegerField(default=-1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarkerContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(db_index=True, max_length=50, blank=True)),
                ('type', models.CharField(default=b'text', max_length=20, choices=[(b'text', b'text'), (b'title', b'title'), (b'image', b'image'), (b'website', b'website'), (b'map', b'map'), (b'video', b'video'), (b'media', b'media'), (b'audio', b'audio'), (b'simple_button', b'simple_button'), (b'social', b'social')])),
                ('ordinal', models.IntegerField(default=0, null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('url', models.CharField(max_length=255, blank=True)),
                ('marker', models.ForeignKey(related_name='contents', to='videos.Marker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayerAppearance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('ui_color_1', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_2', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_playbar_outline', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_playbar_background', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_playbar_progress', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_playbar_buffer', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_playbar_indicators', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_marker_background', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_marker_outline', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_marker_text', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_marker_highlight_background', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_marker_highlight_outline', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_marker_highlight_text', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_button_background', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_button_text', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_button_highlight_background', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_button_highlight_text', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_color_overlay_outline', videopath.apps.common.models.ColorField(max_length=10, null=True, blank=True)),
                ('ui_font_marker', models.CharField(max_length=255, null=True, blank=True)),
                ('ui_font_overlay_titles', models.CharField(max_length=255, null=True, blank=True)),
                ('ui_font_overlay_text', models.CharField(max_length=255, null=True, blank=True)),
                ('endscreen_logo', models.CharField(max_length=255, null=True, blank=True)),
                ('icon', models.CharField(max_length=255, null=True, blank=True)),
                ('language', models.CharField(default=b'en', max_length=50, choices=[(b'en', b'English'), (b'de', b'German'), (b'fr', b'French')])),
                ('sharing_disabled', models.BooleanField(default=False)),
                ('user', models.OneToOneField(related_name='default_player_appearance', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(db_index=True, unique=True, max_length=50, blank=True)),
                ('published', models.IntegerField(default=0, choices=[(0, b'Private'), (1, b'Public')])),
                ('nice_name', models.CharField(db_index=True, max_length=50, blank=True)),
                ('total_plays', models.IntegerField(default=0)),
                ('total_views', models.IntegerField(default=0)),
                ('player_version', models.CharField(default=b'2', max_length=20, choices=[(b'1', b'1 - Scruffy'), (b'2', b'2 - Bender')])),
                ('archived', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoRevision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default=b'New Video', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('video_appearance', models.TextField(blank=True)),
                ('custom_tracking_code', models.CharField(max_length=20, blank=True)),
                ('ui_color_1', videopath.apps.common.models.ColorField(default=b'#424242', max_length=10)),
                ('ui_color_2', videopath.apps.common.models.ColorField(default=b'#ffffff', max_length=10)),
                ('ui_disable_share_buttons', models.BooleanField(default=False)),
                ('ui_equal_marker_lengths', models.BooleanField(default=False)),
                ('ui_fit_video', models.BooleanField(default=False)),
                ('iphone_images', models.IntegerField(default=-1)),
                ('endscreen_url', models.CharField(max_length=512, blank=True)),
                ('endscreen_title', models.CharField(max_length=512, blank=True)),
                ('endscreen_background_color', videopath.apps.common.models.ColorField(default=b'#32526e', max_length=10, blank=True)),
                ('endscreen_button_title', models.CharField(default=b'Try videopath now', max_length=512, blank=True)),
                ('endscreen_button_target', models.CharField(default=b'http://videopath.com', max_length=512, blank=True)),
                ('endscreen_button_color', videopath.apps.common.models.ColorField(default=b'#ff6b57', max_length=10, blank=True)),
                ('endscreen_subtitle', models.CharField(default=b'Create your own interactive video', max_length=512, blank=True)),
                ('custom_thumbnail', models.ForeignKey(related_name='video_thumbnail', default=None, blank=True, to='files.ImageFile', null=True)),
                ('player_appearance', models.ForeignKey(related_name='video_revisions', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='videos.PlayerAppearance', null=True)),
                ('video', models.ForeignKey(related_name='revisions', to='videos.Video')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='video',
            name='current_revision',
            field=models.OneToOneField(related_name='video_current', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='videos.VideoRevision'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='draft',
            field=models.OneToOneField(related_name='video_draft', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='videos.VideoRevision'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='user',
            field=models.ForeignKey(related_name='videos', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='marker',
            name='video_revision',
            field=models.ForeignKey(related_name='markers', to='videos.VideoRevision'),
            preserve_default=True,
        ),
    ]
