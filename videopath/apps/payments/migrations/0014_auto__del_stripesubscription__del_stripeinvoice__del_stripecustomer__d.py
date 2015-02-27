# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'StripeSubscription'
        db.delete_table(u'payments_stripesubscription')

        # Deleting model 'StripeInvoice'
        db.delete_table(u'payments_stripeinvoice')

        # Deleting model 'StripeCustomer'
        db.delete_table(u'payments_stripecustomer')

        # Deleting model 'StripeCard'
        db.delete_table(u'payments_stripecard')

        # Adding model 'StripeID'
        db.create_table(u'payments_stripeid', (
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('key', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=50, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(
                related_name='stripe_id', unique=True, primary_key=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'payments', ['StripeID'])

        # Adding model 'PendingSubscription'
        db.create_table(u'payments_pendingsubscription', (
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('plan', self.gf('django.db.models.fields.CharField')
             (max_length=150)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(
                related_name='pending_subscription', unique=True, primary_key=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'payments', ['PendingSubscription'])

        # Adding model 'Payment'
        db.create_table(u'payments_payment', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('exported_invoice', self.gf(
                'django.db.models.fields.BooleanField')(default=False)),
            ('paid', self.gf('django.db.models.fields.BooleanField')
             (default=False)),
            ('charging_attempts', self.gf(
                'django.db.models.fields.IntegerField')(default=0)),
            ('amount_due', self.gf(
                'django.db.models.fields.IntegerField')(default=0)),
            ('percent_vat', self.gf(
                'django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf(
                'django.db.models.fields.DateTimeField')(null=True)),
            ('number', self.gf(
                'django.db.models.fields.IntegerField')(default=0)),
            ('details', self.gf('django.db.models.fields.CharField')
             (max_length=2048)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='payments', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'payments', ['Payment'])

        # Adding field 'Subscription.current_period_start'
        db.add_column(u'payments_subscription', 'current_period_start',
                      self.gf('django.db.models.fields.DateTimeField')(
                          null=True),
                      keep_default=False)

        # Adding field 'Subscription.current_period_end'
        db.add_column(u'payments_subscription', 'current_period_end',
                      self.gf('django.db.models.fields.DateTimeField')(
                          null=True),
                      keep_default=False)

        # Adding field 'Subscription.cancel_at_period_end'
        db.add_column(u'payments_subscription', 'cancel_at_period_end',
                      self.gf('django.db.models.fields.BooleanField')(
                          default=False),
                      keep_default=False)

    def backwards(self, orm):
        # Adding model 'StripeSubscription'
        db.create_table(u'payments_stripesubscription', (
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='subscriptions', null=True, to=orm['payments.StripeCustomer'], blank=True)),
            ('cancel_at_period_end', self.gf(
                'django.db.models.fields.BooleanField')(default=False)),
            ('plan', self.gf('django.db.models.fields.CharField')
             (max_length=50, db_index=True)),
            ('key', self.gf('django.db.models.fields.CharField')
             (max_length=50, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('current_period_start', self.gf(
                'django.db.models.fields.DateTimeField')(null=True)),
            ('current_period_end', self.gf(
                'django.db.models.fields.DateTimeField')(null=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
        ))
        db.send_create_signal(u'payments', ['StripeSubscription'])

        # Adding model 'StripeInvoice'
        db.create_table(u'payments_stripeinvoice', (
            ('number', self.gf(
                'django.db.models.fields.IntegerField')(default=0)),
            ('paid', self.gf('django.db.models.fields.BooleanField')
             (default=False)),
            ('exported', self.gf(
                'django.db.models.fields.BooleanField')(default=False)),
            ('key', self.gf('django.db.models.fields.CharField')
             (max_length=50, unique=True, db_index=True)),
            ('date', self.gf(
                'django.db.models.fields.DateTimeField')(null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='invoices', null=True, to=orm['payments.StripeCustomer'], blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('amount_due', self.gf(
                'django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'payments', ['StripeInvoice'])

        # Adding model 'StripeCustomer'
        db.create_table(u'payments_stripecustomer', (
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='stripe_customers', to=orm['auth.User'])),
            ('key', self.gf('django.db.models.fields.CharField')
             (max_length=50, unique=True, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
        ))
        db.send_create_signal(u'payments', ['StripeCustomer'])

        # Adding model 'StripeCard'
        db.create_table(u'payments_stripecard', (
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='cards', null=True, to=orm['payments.StripeCustomer'], blank=True)),
            ('last4', self.gf('django.db.models.fields.CharField')
             (max_length=10)),
            ('key', self.gf('django.db.models.fields.CharField')
             (max_length=50, unique=True, db_index=True)),
            ('exp_month', self.gf(
                'django.db.models.fields.IntegerField')(default=1)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('exp_year', self.gf(
                'django.db.models.fields.IntegerField')(default=2012)),
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'payments', ['StripeCard'])

        # Deleting model 'StripeID'
        db.delete_table(u'payments_stripeid')

        # Deleting model 'PendingSubscription'
        db.delete_table(u'payments_pendingsubscription')

        # Deleting model 'Payment'
        db.delete_table(u'payments_payment')

        # Deleting field 'Subscription.current_period_start'
        db.delete_column(u'payments_subscription', 'current_period_start')

        # Deleting field 'Subscription.current_period_end'
        db.delete_column(u'payments_subscription', 'current_period_end')

        # Deleting field 'Subscription.cancel_at_period_end'
        db.delete_column(u'payments_subscription', 'cancel_at_period_end')

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
        u'payments.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount_due': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'charging_attempts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'exported_invoice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'percent_vat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'cancel_at_period_end': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_period_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'current_period_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'managed_by': ('django.db.models.fields.CharField', [], {'default': "'admin'", 'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'plan': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'subscription'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['payments']
