# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0022_auto_20180828_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sent_item',
            name='sender_id',
            field=models.CharField(max_length=50),
        ),
    ]
