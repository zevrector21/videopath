# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'StripeCard.user'
        db.delete_column(u'payments_stripecard', 'user_id')

        # Adding field 'StripeCard.customer'
        db.add_column(u'payments_stripecard', 'customer',
                      self.gf('django.db.models.fields.related.OneToOneField')(
                          blank=True, related_name='card', unique=True, null=True, to=orm['payments.StripeCustomer']),
                      keep_default=False)

        # Deleting field 'StripeInvoice.user'
        db.delete_column(u'payments_stripeinvoice', 'user_id')

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for
        # 'StripeCard.user'
        raise RuntimeError(
            "Cannot reverse this migration. 'StripeCard.user' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct
        # migration        # Adding field 'StripeCard.user'
        db.add_column(u'payments_stripecard', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(
                          related_name='stripe_card', unique=True, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'StripeCard.customer'
        db.delete_column(u'payments_stripecard', 'customer_id')

        # User chose to not deal with backwards NULL issues for
        # 'StripeInvoice.user'
        raise RuntimeError(
            "Cannot reverse this migration. 'StripeInvoice.user' and its values cannot be restored.")

        # The following code is provided here to aid in writing a correct
        # migration        # Adding field 'StripeInvoice.user'
        db.add_column(u'payments_stripeinvoice', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(
                          related_name='stripe_invoice', unique=True, to=orm['auth.User']),
                      keep_default=False)

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
        u'payments.paymentdetails': {
            'Meta': {'object_name': 'PaymentDetails'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'post_code': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'payment_details'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'payments.stripecard': {
            'Meta': {'object_name': 'StripeCard'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'card'", 'unique': 'True', 'null': 'True', 'to': u"orm['payments.StripeCustomer']"}),
            'exp_month': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'exp_year': ('django.db.models.fields.IntegerField', [], {'default': '2012'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'payments.stripecustomer': {
            'Meta': {'object_name': 'StripeCustomer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'stripe_customer'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'payments.stripeinvoice': {
            'Meta': {'object_name': 'StripeInvoice'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'payments.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'plan': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'subscription'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['payments']
