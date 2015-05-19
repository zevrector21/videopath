# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Payment.currency'
        db.add_column(u'payments_payment', 'currency',
                      self.gf('django.db.models.fields.CharField')(default='EUR', max_length=3),
                      keep_default=False)

        # Deleting field 'Subscription.custom_price_periods_remaining'
        db.delete_column(u'payments_subscription', 'custom_price_periods_remaining')

        # Adding field 'Subscription.currency'
        db.add_column(u'payments_subscription', 'currency',
                      self.gf('django.db.models.fields.CharField')(default='EUR', max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Payment.currency'
        db.delete_column(u'payments_payment', 'currency')

        # Adding field 'Subscription.custom_price_periods_remaining'
        db.add_column(u'payments_subscription', 'custom_price_periods_remaining',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Subscription.currency'
        db.delete_column(u'payments_subscription', 'currency')


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
        u'payments.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount_due': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'charging_attempts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'exported_invoice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_charging_attempt': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'percent_vat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'provider': ('django.db.models.fields.CharField', [], {'default': "'other'", 'max_length': '150'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payments'", 'to': u"orm['auth.User']"})
        },
        u'payments.paymentdetails': {
            'Meta': {'object_name': 'PaymentDetails'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'payment_details'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"})
        },
        u'payments.pendingsubscription': {
            'Meta': {'object_name': 'PendingSubscription'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'plan': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'pending_subscription'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"})
        },
        u'payments.quotainformation': {
            'Meta': {'object_name': 'QuotaInformation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'quota_exceeded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'quota_info'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"}),
            'warning_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'payments.stripeid': {
            'Meta': {'object_name': 'StripeID'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'stripe_id'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"})
        },
        u'payments.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'current_period_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'current_period_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'custom_price': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'managed_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'plan': ('django.db.models.fields.CharField', [], {'default': "'free-free'", 'max_length': '150'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'subscription'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['payments']