# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20151005_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercampaigndata',
            name='content',
            field=models.CharField(default=b'', max_length=512, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usercampaigndata',
            name='country',
            field=models.CharField(default=b'', max_length=512, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usercampaigndata',
            name='medium',
            field=models.CharField(default=b'', max_length=512, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usercampaigndata',
            name='name',
            field=models.CharField(default=b'', max_length=512, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usercampaigndata',
            name='referrer',
            field=models.CharField(default=b'', max_length=512, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usercampaigndata',
            name='source',
            field=models.CharField(default=b'', max_length=512, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usercampaigndata',
            name='term',
            field=models.CharField(default=b'', max_length=512, null=True),
            preserve_default=True,
        ),
    ]
