# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0008_auto_20170724_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='subject',
        ),
        migrations.AlterField(
            model_name='inbox',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
