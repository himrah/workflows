# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Workflow', '0020_sent_item_is_read'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('subject', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('receiver_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='alert',
            name='receiver_id',
        ),
        migrations.DeleteModel(
            name='Alert',
        ),
    ]
