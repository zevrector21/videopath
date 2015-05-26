# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userena.models
from django.conf import settings
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationToken',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('last_used', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='authentication_tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AutomatedMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('mailtype', models.CharField(default=b'', max_length=20, choices=[(b'welcome', b'welcome'), (b'retention1', b'retention1'), (b'retention2', b'retention2'), (b'retention3', b'retention3')])),
                ('user', models.ForeignKey(related_name='automated_mails', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OneTimeAuthenticationToken',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('token', models.ForeignKey(related_name='onetime_tokens', to='users.AuthenticationToken')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('last_seen', models.DateTimeField(null=True, blank=True)),
                ('user', models.OneToOneField(related_name='activity', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserActivityDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('day', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(related_name='user_activity_day', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mugshot', easy_thumbnails.fields.ThumbnailerImageField(help_text='A personal image displayed in your profile.', upload_to=userena.models.upload_to_mugshot, verbose_name='mugshot', blank=True)),
                ('privacy', models.CharField(default=b'registered', help_text='Designates who can view your profile.', max_length=15, verbose_name='privacy', choices=[(b'open', 'Open'), (b'registered', 'Registered'), (b'closed', 'Closed')])),
                ('currency', models.CharField(default=b'EUR', max_length=3, choices=[(b'USD', b'US Dollars'), (b'EUR', b'Euro')])),
                ('user', models.OneToOneField(related_name='settings', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Settings',
                'verbose_name_plural': 'User Settings',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='useractivityday',
            unique_together=set([('user', 'day')]),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
        ),
    ]
