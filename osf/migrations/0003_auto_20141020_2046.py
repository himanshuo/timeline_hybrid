# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0002_auto_20141020_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='wiki',
            field=models.TextField(null=True, blank=True),
        ),
    ]
