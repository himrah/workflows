# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0016_auto_20170901_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%d/'),
        ),
    ]
