# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0013_auto_20170830_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
