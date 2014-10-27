# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0003_auto_20141020_2046'),
    ]

    operations = [
        migrations.DeleteModel(
            name='History',
        ),
    ]
