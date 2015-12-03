# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_auto_20151124_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default=b'My Projects', max_length=150)),
                ('is_default_team_of_user', models.OneToOneField(related_name='default_team', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('member_type', models.CharField(default=b'editor', max_length=20, choices=[(b'editor', b'editor'), (b'admin', b'admin')])),
                ('team', models.ForeignKey(to='users.Team')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='users.TeamMember'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(related_name='owned_teams', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
