# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0017_auto_20170901_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='file',
        ),
    ]
