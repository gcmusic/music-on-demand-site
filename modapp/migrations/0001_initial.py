# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('reg_date', models.DateTimeField(verbose_name='Date registered')),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]