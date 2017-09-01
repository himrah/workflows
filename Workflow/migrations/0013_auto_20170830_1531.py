# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0012_auto_20170824_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(null=True, default=datetime.datetime.now),
        ),
    ]
