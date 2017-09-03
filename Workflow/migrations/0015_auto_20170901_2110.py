# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0014_task_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.ImageField(upload_to='photos/%d/', blank=True, null=True),
        ),
    ]
