# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0011_auto_20170824_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='modify_by',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
