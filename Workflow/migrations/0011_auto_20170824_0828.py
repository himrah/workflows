# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0010_inbox_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sent_item',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
