# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PlayerAppearance.user'
        db.alter_column(u'videos_playerappearance', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['auth.User']))

        # Changing field 'PlayerAppearance.video_revision'
        db.alter_column(u'videos_playerappearance', 'video_revision_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['videos.VideoRevision']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'PlayerAppearance.user'
        raise RuntimeError("Cannot reverse this migration. 'PlayerAppearance.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'PlayerAppearance.user'
        db.alter_column(u'videos_playerappearance', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User']))

        # User chose to not deal with backwards NULL issues for 'PlayerAppearance.video_revision'
        raise RuntimeError("Cannot reverse this migration. 'PlayerAppearance.video_revision' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'PlayerAppearance.video_revision'
        db.alter_column(u'videos_playerappearance', 'video_revision_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['videos.VideoRevision']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'files.imagefile': {
            'Meta': {'object_name': 'ImageFile'},
            'bytes': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_type': ('django.db.models.fields.CharField', [], {'default': "'marker content'", 'max_length': '255', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'markercontent': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'image_file'", 'blank': 'True', 'to': "orm['videos.MarkerContent']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'original_file_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'videos.marker': {
            'Meta': {'object_name': 'Marker'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'overlay_height': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'overlay_width': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'time': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'video_revision': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'markers'", 'to': "orm['videos.VideoRevision']"})
        },
        'videos.markercontent': {
            'Meta': {'object_name': 'MarkerContent'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'marker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contents'", 'to': "orm['videos.Marker']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ordinal': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '20'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'videos.playerappearance': {
            'Meta': {'object_name': 'PlayerAppearance'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'endscreen_logo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '50'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'sharing_disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ui_color_1': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_2': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_button_background': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_button_highlight_background': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_button_highlight_text': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_button_text': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_marker_background': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_marker_highlight_background': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_marker_highlight_outline': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_marker_highlight_text': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_marker_outline': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_marker_text': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_overlay_outline': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_playbar_background': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_playbar_buffer': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_playbar_outline': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_color_playbar_progress': ('videopath.apps.common.models.ColorField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'ui_font_marker': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ui_font_overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ui_font_overlay_titles': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'default_player_appearance'", 'unique': 'True', 'null': 'True', 'to': u"orm['auth.User']"}),
            'video_revision': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'appearance'", 'unique': 'True', 'null': 'True', 'to': "orm['videos.VideoRevision']"})
        },
        'videos.video': {
            'Meta': {'object_name': 'Video'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_revision': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'video_current'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['videos.VideoRevision']", 'blank': 'True', 'unique': 'True'}),
            'draft': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'video_draft'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['videos.VideoRevision']", 'blank': 'True', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nice_name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'player_version': ('django.db.models.fields.CharField', [], {'default': "'2'", 'max_length': '20'}),
            'published': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_plays': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_views': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': u"orm['auth.User']"})
        },
        'videos.videorevision': {
            'Meta': {'object_name': 'VideoRevision'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'custom_logo': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'video_logo'", 'null': 'True', 'blank': 'True', 'to': u"orm['files.ImageFile']"}),
            'custom_thumbnail': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'video_thumbnail'", 'null': 'True', 'blank': 'True', 'to': u"orm['files.ImageFile']"}),
            'custom_tracking_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'endscreen_background_color': ('videopath.apps.common.models.ColorField', [], {'default': "'#32526e'", 'max_length': '10', 'blank': 'True'}),
            'endscreen_button_color': ('videopath.apps.common.models.ColorField', [], {'default': "'#ff6b57'", 'max_length': '10', 'blank': 'True'}),
            'endscreen_button_target': ('django.db.models.fields.CharField', [], {'default': "'http://videopath.com'", 'max_length': '512', 'blank': 'True'}),
            'endscreen_button_title': ('django.db.models.fields.CharField', [], {'default': "'Try videopath now'", 'max_length': '512', 'blank': 'True'}),
            'endscreen_subtitle': ('django.db.models.fields.CharField', [], {'default': "'Create your own interactive video'", 'max_length': '512', 'blank': 'True'}),
            'endscreen_title': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'endscreen_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iphone_images': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'revision_number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'New Video'", 'max_length': '255'}),
            'ui_color_1': ('videopath.apps.common.models.ColorField', [], {'default': "'#424242'", 'max_length': '10'}),
            'ui_color_2': ('videopath.apps.common.models.ColorField', [], {'default': "'#ffffff'", 'max_length': '10'}),
            'ui_disable_share_buttons': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ui_equal_marker_lengths': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ui_fit_video': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ui_marker_font': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'ui_overlay_content_font': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'ui_overlay_title_font': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'revisions'", 'to': "orm['videos.Video']"}),
            'video_appearance': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['videos']