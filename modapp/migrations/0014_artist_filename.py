# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modapp', '0013_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='filename',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
