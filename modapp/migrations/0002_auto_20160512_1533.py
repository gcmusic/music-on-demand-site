# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 12:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='name',
        ),
    ]
