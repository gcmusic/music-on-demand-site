# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modapp', '0011_auto_20160702_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='artist_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]