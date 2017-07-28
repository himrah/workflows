# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Workflow', '0004_auto_20170721_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='altr_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='D_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='email_msg',
            old_name='msg_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='inbox',
            old_name='msg_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='prj_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='sent_item',
            old_name='msg_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_id',
            new_name='id',
        ),
    ]
