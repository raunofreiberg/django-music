# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170518_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='isFavorite',
            field=models.BooleanField(default=False),
        ),
    ]