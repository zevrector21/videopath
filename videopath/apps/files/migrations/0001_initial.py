# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageFile'
        db.create_table(u'files_imagefile', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=50, blank=True)),
            ('width', self.gf(
                'django.db.models.fields.SmallIntegerField')(default=0)),
            ('height', self.gf(
                'django.db.models.fields.SmallIntegerField')(default=0)),
            ('bytes', self.gf(
                'django.db.models.fields.BigIntegerField')(default=0)),
            ('status', self.gf(
                'django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'files', ['ImageFile'])

        # Adding M2M table for field markercontent on 'ImageFile'
        m2m_table_name = db.shorten_name(u'files_imagefile_markercontent')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(
                verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagefile', models.ForeignKey(
                orm[u'files.imagefile'], null=False)),
            ('markercontent', models.ForeignKey(
                orm[u'videos.markercontent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['imagefile_id', 'markercontent_id'])

        # Adding model 'VideoFile'
        db.create_table(u'files_videofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=50, blank=True)),
            ('transcoding_job_id', self.gf('django.db.models.fields.CharField')(
                max_length=255, blank=True)),
            ('video_width', self.gf(
                'django.db.models.fields.SmallIntegerField')(default=0)),
            ('video_height', self.gf(
                'django.db.models.fields.SmallIntegerField')(default=0)),
            ('video_duration', self.gf(
                'django.db.models.fields.FloatField')(default=0)),
            ('transcoding_result', self.gf('django.db.models.fields.CharField')(
                max_length=255, blank=True)),
            ('status', self.gf(
                'django.db.models.fields.SmallIntegerField')(default=0)),
            ('bytes', self.gf(
                'django.db.models.fields.BigIntegerField')(default=0)),
            ('video', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='file', to=orm['videos.Video'])),
        ))
        db.send_create_signal(u'files', ['VideoFile'])

    def backwards(self, orm):
        # Deleting model 'ImageFile'
        db.delete_table(u'files_imagefile')

        # Removing M2M table for field markercontent on 'ImageFile'
        db.delete_table(db.shorten_name(u'files_imagefile_markercontent'))

        # Deleting model 'VideoFile'
        db.delete_table(u'files_videofile')

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
            'markercontent': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'image_file'", 'symmetrical': 'False', 'to': u"orm['videos.MarkerContent']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'files.videofile': {
            'Meta': {'object_name': 'VideoFile'},
            'bytes': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'transcoding_job_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'transcoding_result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'file'", 'to': u"orm['videos.Video']"}),
            'video_duration': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'video_height': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'video_width': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        u'videos.marker': {
            'Meta': {'object_name': 'Marker'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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
            'current_revision': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'video_current'", 'null': 'True', 'to': u"orm['videos.VideoRevision']"}),
            'draft': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'video_draft'", 'null': 'True', 'to': u"orm['videos.VideoRevision']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videos'", 'to': u"orm['auth.User']"})
        },
        u'videos.videorevision': {
            'Meta': {'object_name': 'VideoRevision'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'revision_number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'New Video'", 'max_length': '50'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'revisions'", 'to': u"orm['videos.Video']"})
        }
    }

    complete_apps = ['files']
