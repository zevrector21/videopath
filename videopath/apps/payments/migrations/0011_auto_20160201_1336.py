# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_auto_20160119_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingsubscription',
            name='plan',
            field=models.CharField(max_length=150, choices=[(b'free-free', b'1000 Free (free-free)'), (b'201509-starter-monthly-15', b'2001 Basic Monthly (201509-starter-monthly-15)'), (b'201509-starter-monthly-20-discount', b'2002 Basic Monthly (20% Partners Discount) (201509-starter-monthly-20-discount)'), (b'201509-starter-monthly', b'2003 Basic Monthly (201509-starter-monthly)'), (b'201509-starter-yearly-20-discount', b'2004 Basic Yearly (20% Partners Discount) (201509-starter-yearly-20-discount)'), (b'201509-starter-yearly', b'2005 Basic Yearly (201509-starter-yearly)'), (b'201412-pro-plus-monthly-25-jobviddy', b'4001 Professional Monthly (25% Discount) Andy (201412-pro-plus-monthly-25-jobviddy)'), (b'201412-pro-plus-monthly-20-discount', b'4002 Professional Monthly (20% Partners Discount) (201412-pro-plus-monthly-20-discount)'), (b'201412-pro-plus-monthly', b'4003 Professional Monthly (201412-pro-plus-monthly)'), (b'201412-pro-plus-yearly-20-discount', b'4004 Professional Yearly (20% Partners Discount) (201412-pro-plus-yearly-20-discount)'), (b'201412-pro-plus-yearly', b'4005 Professional Yearly (201412-pro-plus-yearly)'), (b'201412-enterprise-monthly-20-discount', b'6001 Enterprise Monthly (20% Partners Discount) (201412-enterprise-monthly-20-discount)'), (b'201412-enterprise-monthly', b'6002 Enterprise Monthly (201412-enterprise-monthly)'), (b'201412-enterprise-yearly-20-discount', b'6003 Enterprise Yearly (20% Partners Discount) (201412-enterprise-yearly-20-discount)'), (b'201412-enterprise-yearly', b'6004 Enterprise Yearly (201412-enterprise-yearly)'), (b'individual-individual', b'8000 Individual Plan (individual-individual)'), (b'individual-meisterclass', b'8001 Individual meisterclasss (individual-meisterclass)'), (b'individual-escp', b'8002 Individual escp (individual-escp)'), (b'individual-sspss', b'8003 Individual SSPSS (individual-sspss)'), (b'individual-agency-evaluation', b'8004 Agency Evaluation (individual-agency-evaluation)'), (b'individual-staff', b'9999 videopath staff account (individual-staff)')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.CharField(default=b'free-free', max_length=150, choices=[(b'free-free', b'1000 Free (free-free)'), (b'201509-starter-monthly-15', b'2001 Basic Monthly (201509-starter-monthly-15)'), (b'201509-starter-monthly-20-discount', b'2002 Basic Monthly (20% Partners Discount) (201509-starter-monthly-20-discount)'), (b'201509-starter-monthly', b'2003 Basic Monthly (201509-starter-monthly)'), (b'201509-starter-yearly-20-discount', b'2004 Basic Yearly (20% Partners Discount) (201509-starter-yearly-20-discount)'), (b'201509-starter-yearly', b'2005 Basic Yearly (201509-starter-yearly)'), (b'201412-pro-plus-monthly-25-jobviddy', b'4001 Professional Monthly (25% Discount) Andy (201412-pro-plus-monthly-25-jobviddy)'), (b'201412-pro-plus-monthly-20-discount', b'4002 Professional Monthly (20% Partners Discount) (201412-pro-plus-monthly-20-discount)'), (b'201412-pro-plus-monthly', b'4003 Professional Monthly (201412-pro-plus-monthly)'), (b'201412-pro-plus-yearly-20-discount', b'4004 Professional Yearly (20% Partners Discount) (201412-pro-plus-yearly-20-discount)'), (b'201412-pro-plus-yearly', b'4005 Professional Yearly (201412-pro-plus-yearly)'), (b'201412-enterprise-monthly-20-discount', b'6001 Enterprise Monthly (20% Partners Discount) (201412-enterprise-monthly-20-discount)'), (b'201412-enterprise-monthly', b'6002 Enterprise Monthly (201412-enterprise-monthly)'), (b'201412-enterprise-yearly-20-discount', b'6003 Enterprise Yearly (20% Partners Discount) (201412-enterprise-yearly-20-discount)'), (b'201412-enterprise-yearly', b'6004 Enterprise Yearly (201412-enterprise-yearly)'), (b'individual-individual', b'8000 Individual Plan (individual-individual)'), (b'individual-meisterclass', b'8001 Individual meisterclasss (individual-meisterclass)'), (b'individual-escp', b'8002 Individual escp (individual-escp)'), (b'individual-sspss', b'8003 Individual SSPSS (individual-sspss)'), (b'individual-agency-evaluation', b'8004 Agency Evaluation (individual-agency-evaluation)'), (b'individual-staff', b'9999 videopath staff account (individual-staff)')]),
            preserve_default=True,
        ),
    ]
