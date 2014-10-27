# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, null=True, blank=True)),
                ('author', models.CharField(max_length=256, null=True, blank=True)),
                ('wiki', models.TextField(max_length=256, null=True, blank=True)),
                ('date', models.DateTimeField()),
                ('project_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, null=True, blank=True)),
                ('author', models.CharField(max_length=256, null=True, blank=True)),
                ('wiki', models.TextField(null=True, blank=True)),
                ('project_id', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
