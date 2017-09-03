# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Workflow.models


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0015_auto_20170901_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.ImageField(null=True, upload_to=Workflow.models.upload_path_handler, blank=True),
        ),
    ]
