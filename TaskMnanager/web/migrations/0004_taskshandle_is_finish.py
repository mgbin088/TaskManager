# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-01 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_taskshandle_task_cc2'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskshandle',
            name='is_finish',
            field=models.BooleanField(default=0),
        ),
    ]
