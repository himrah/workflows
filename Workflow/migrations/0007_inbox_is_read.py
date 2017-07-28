# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0006_inbox_sender_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbox',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
