# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modapp', '0008_artist_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='total_stars',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
