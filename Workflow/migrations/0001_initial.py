# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('altr_id', models.AutoField(serialize=False, primary_key=True)),
                ('subject', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('receiver_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('D_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('head', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Email_msg',
            fields=[
                ('msg_id', models.AutoField(serialize=False, primary_key=True)),
                ('sender_id', models.CharField(max_length=20)),
                ('subject', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('receiver_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('msg_id', models.AutoField(serialize=False, primary_key=True)),
                ('subject', models.TextField()),
                ('content', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('receiver_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('prj_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sent_item',
            fields=[
                ('msg_id', models.AutoField(serialize=False, primary_key=True)),
                ('sender_id', models.CharField(max_length=20)),
                ('subject', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('receiver_id', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('created_by', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('New', 'New'), ('In Process', 'In Process'), ('Complete', 'Complete')], default='----', max_length=10)),
                ('task_description', models.TextField()),
                ('comments', models.TextField(blank=True)),
                ('modify_by', models.CharField(max_length=20)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Low', 'Low'), ('Normal', 'Normal')], default='----', max_length=10)),
                ('tat', models.IntegerField()),
                ('assign', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('project_id', models.ForeignKey(to='Workflow.Project', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='project',
            field=models.ForeignKey(to='Workflow.Project', null=True),
        ),
    ]
