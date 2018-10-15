# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0021_auto_20170922_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='sender_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
