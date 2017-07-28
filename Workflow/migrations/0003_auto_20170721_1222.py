# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0002_auto_20170721_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='head',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
