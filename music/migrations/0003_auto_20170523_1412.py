# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20170523_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
            preserve_default=False,
        ),
    ]