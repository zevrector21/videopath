# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StripeInvoice.customer'
        db.add_column(u'payments_stripeinvoice', 'customer',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          blank=True, related_name='invoices', null=True, to=orm['payments.StripeCustomer']),
                      keep_default=False)

        # Adding field 'StripeInvoice.amount_due'
        db.add_column(u'payments_stripeinvoice', 'amount_due',
                      self.gf('django.db.models.fields.IntegerField')(
                          default=0),
                      keep_default=False)

        # Adding field 'StripeInvoice.date'
        db.add_column(u'payments_stripeinvoice', 'date',
                      self.gf('django.db.models.fields.DateTimeField')(
                          null=True),
                      keep_default=False)

        # Adding field 'StripeInvoice.paid'
        db.add_column(u'payments_stripeinvoice', 'paid',
                      self.gf('django.db.models.fields.BooleanField')(
                          default=False),
                      keep_default=False)

        # Adding field 'StripeInvoice.exported'
        db.add_column(u'payments_stripeinvoice', 'exported',
                      self.gf('django.db.models.fields.BooleanField')(
                          default=False),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'StripeInvoice.customer'
        db.delete_column(u'payments_stripeinvoice', 'customer_id')

        # Deleting field 'StripeInvoice.amount_due'
        db.delete_column(u'payments_stripeinvoice', 'amount_due')

        # Deleting field 'StripeInvoice.date'
        db.delete_column(u'payments_stripeinvoice', 'date')

        # Deleting field 'StripeInvoice.paid'
        db.delete_column(u'payments_stripeinvoice', 'paid')

        # Deleting field 'StripeInvoice.exported'
        db.delete_column(u'payments_stripeinvoice', 'exported')

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
            'amount_due': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoices'", 'null': 'True', 'to': u"orm['payments.StripeCustomer']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'exported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
