# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170523_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='fileType',
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.CharField(max_length=1000),
        ),
    ]
