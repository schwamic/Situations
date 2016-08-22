# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20160819_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.AddField(
            model_name='image',
            name='filename',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]