# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0005_auto_20170721_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbox',
            name='sender_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
