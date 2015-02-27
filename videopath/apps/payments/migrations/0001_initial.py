# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StripeCustomer'
        db.create_table(u'payments_stripecustomer', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=50, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(
                related_name='stripe_customer', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'payments', ['StripeCustomer'])

        # Adding model 'StripeCard'
        db.create_table(u'payments_stripecard', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=50, db_index=True)),
            ('last4', self.gf('django.db.models.fields.CharField')
             (max_length=10)),
            ('exp_month', self.gf(
                'django.db.models.fields.IntegerField')(default=1)),
            ('exp_year', self.gf(
                'django.db.models.fields.IntegerField')(default=2012)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')
             (related_name='stripe_card', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'payments', ['StripeCard'])

        # Adding model 'StripeInvoice'
        db.create_table(u'payments_stripeinvoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=50, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(
                related_name='stripe_invoice', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'payments', ['StripeInvoice'])

        # Adding model 'PaymentDetails'
        db.create_table(u'payments_paymentdetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')
             (max_length=150)),
            ('street', self.gf('django.db.models.fields.CharField')
             (max_length=150)),
            ('city', self.gf('django.db.models.fields.CharField')
             (max_length=150)),
            ('post_code', self.gf(
                'django.db.models.fields.CharField')(max_length=150)),
            ('country', self.gf('django.db.models.fields.CharField')
             (max_length=150)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(
                related_name='payment_details', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'payments', ['PaymentDetails'])

        # Adding model 'Subscription'
        db.create_table(u'payments_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('plan', self.gf('django.db.models.fields.CharField')
             (max_length=50, db_index=True)),
            ('external_id', self.gf('django.db.models.fields.CharField')
             (max_length=50, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')
             (related_name='subscription', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'payments', ['Subscription'])

    def backwards(self, orm):
        # Deleting model 'StripeCustomer'
        db.delete_table(u'payments_stripecustomer')

        # Deleting model 'StripeCard'
        db.delete_table(u'payments_stripecard')

        # Deleting model 'StripeInvoice'
        db.delete_table(u'payments_stripeinvoice')

        # Deleting model 'PaymentDetails'
        db.delete_table(u'payments_paymentdetails')

        # Deleting model 'Subscription'
        db.delete_table(u'payments_subscription')

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
            'exp_month': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'exp_year': ('django.db.models.fields.IntegerField', [], {'default': '2012'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'stripe_card'", 'unique': 'True', 'to': u"orm['auth.User']"})
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
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'stripe_invoice'", 'unique': 'True', 'to': u"orm['auth.User']"})
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
