# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0009_auto_20170729_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbox',
            name='subject',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
