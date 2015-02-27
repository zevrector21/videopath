# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'VideoSource.video'
        db.alter_column(u'files_videosource', 'video_id', self.gf(
            'django.db.models.fields.related.ForeignKey')(null=True, to=orm['videos.Video']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for
        # 'VideoSource.video'
        raise RuntimeError(
            "Cannot reverse this migration. 'VideoSource.video' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct migration
        # Changing field 'VideoSource.video'
        db.alter_column(u'files_videosource', 'video_id', self.gf(
            'django.db.models.fields.related.ForeignKey')(to=orm['videos.Video']))

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
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
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'markercontent': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'image_file'", 'blank': 'True', 'to': u"orm['videos.MarkerContent']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'original_file_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'files.videofile': {
            'Meta': {'object_name': 'VideoFile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'original_bytes': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'original_file_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'thumbnail_index': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'transcoded_bytes': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'transcoding_job_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'transcoding_result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'file'", 'to': u"orm['videos.Video']"}),
            'video_aspect': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'video_duration': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'video_height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'video_width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'files.videosource': {
            'Meta': {'object_name': 'VideoSource'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '255'}),
            'service_identifier': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'thumbnail_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2048'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'video_sources'", 'null': 'True', 'to': u"orm['videos.Video']"}),
            'video_aspect': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'video_duration': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'videos.marker': {
            'Meta': {'object_name': 'Marker'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'overlay_height': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'overlay_width': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'time': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'video_revision': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'markers'", 'to': u"orm['videos.VideoRevision']"})
        },
        u'videos.markercontent': {
            'Meta': {'object_name': 'MarkerContent'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contents'", 'to': u"orm['videos.Marker']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'ordinal': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '20'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'videos.video': {
            'Meta': {'object_name': 'Video'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_revision': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'video_current'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['videos.VideoRevision']", 'blank': 'True', 'unique': 'True'}),
            'draft': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'video_draft'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['videos.VideoRevision']", 'blank': 'True', 'unique': 'True'}),
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
        u'videos.videorevision': {
            'Meta': {'object_name': 'VideoRevision'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'endscreen_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'revision_number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'theme': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'New Video'", 'max_length': '50'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'revisions'", 'to': u"orm['videos.Video']"})
        }
    }

    complete_apps = ['files']
