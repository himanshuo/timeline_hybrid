# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='wiki',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='wiki',
            field=models.TextField(max_length=9999, null=True, blank=True),
        ),
    ]
