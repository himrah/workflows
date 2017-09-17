# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0019_auto_20170902_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='sent_item',
            name='is_read',
            field=models.BooleanField(default=True),
        ),
    ]
