# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_auto_20151203_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='vat_id',
            field=models.CharField(default=b'', max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pendingsubscription',
            name='plan',
            field=models.CharField(max_length=150, choices=[(b'free-free', b'0001 Free (free-free)'), (b'201509-starter-monthly-15', b'0009 Basic Monthly (201509-starter-monthly-15)'), (b'201410-starter-monthly', b'0010 Basic Monthly (201410-starter-monthly)'), (b'201412-starter-monthly', b'0010 Basic Monthly (201412-starter-monthly)'), (b'201509-starter-monthly', b'0010 Basic Monthly (201509-starter-monthly)'), (b'201509-starter-yearly', b'0011 Basic Yearly (201509-starter-yearly)'), (b'201412-pro-plus-monthly-25', b'0149 Professional Plus Monthly (25% Discount) (201412-pro-plus-monthly-25)'), (b'201412-pro-plus-monthly-25-jobviddy', b'0149 Professional Plus Monthly (25% Discount) Andy (201412-pro-plus-monthly-25-jobviddy)'), (b'201412-pro-plus-monthly', b'0150 Professional Plus Monthly (201412-pro-plus-monthly)'), (b'201412-pro-plus-yearly', b'0151 Professional Plus Yearly (201412-pro-plus-yearly)'), (b'201412-enterprise-monthly', b'0200 Enterprise Monthly (201412-enterprise-monthly)'), (b'201412-enterprise-yearly', b'0201 Enterprise Yearly (201412-enterprise-yearly)'), (b'individual-staff', b'9999 videopath staff account (individual-staff)'), (b'individual-escp', b'9999 Individual escp (individual-escp)'), (b'individual-agency-evaluation', b'9999 Agency Evaluation (individual-agency-evaluation)'), (b'individual-individual', b'9999 Individual Plan (individual-individual)'), (b'individual-meisterclass', b'9999 Individual meisterclasss (individual-meisterclass)'), (b'individual-sspss', b'9999 Individual SSPSS (individual-sspss)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.CharField(default=b'free-free', max_length=150, choices=[(b'free-free', b'0001 Free (free-free)'), (b'201509-starter-monthly-15', b'0009 Basic Monthly (201509-starter-monthly-15)'), (b'201410-starter-monthly', b'0010 Basic Monthly (201410-starter-monthly)'), (b'201412-starter-monthly', b'0010 Basic Monthly (201412-starter-monthly)'), (b'201509-starter-monthly', b'0010 Basic Monthly (201509-starter-monthly)'), (b'201509-starter-yearly', b'0011 Basic Yearly (201509-starter-yearly)'), (b'201412-pro-plus-monthly-25', b'0149 Professional Plus Monthly (25% Discount) (201412-pro-plus-monthly-25)'), (b'201412-pro-plus-monthly-25-jobviddy', b'0149 Professional Plus Monthly (25% Discount) Andy (201412-pro-plus-monthly-25-jobviddy)'), (b'201412-pro-plus-monthly', b'0150 Professional Plus Monthly (201412-pro-plus-monthly)'), (b'201412-pro-plus-yearly', b'0151 Professional Plus Yearly (201412-pro-plus-yearly)'), (b'201412-enterprise-monthly', b'0200 Enterprise Monthly (201412-enterprise-monthly)'), (b'201412-enterprise-yearly', b'0201 Enterprise Yearly (201412-enterprise-yearly)'), (b'individual-staff', b'9999 videopath staff account (individual-staff)'), (b'individual-escp', b'9999 Individual escp (individual-escp)'), (b'individual-agency-evaluation', b'9999 Agency Evaluation (individual-agency-evaluation)'), (b'individual-individual', b'9999 Individual Plan (individual-individual)'), (b'individual-meisterclass', b'9999 Individual meisterclasss (individual-meisterclass)'), (b'individual-sspss', b'9999 Individual SSPSS (individual-sspss)')]),
            preserve_default=True,
        ),
    ]
