# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='head',
            field=models.ForeignKey(null=True, to='Workflow.Department'),
        ),
    ]
