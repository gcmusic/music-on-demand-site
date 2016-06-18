# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modapp', '0005_auto_20160611_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='location',
            field=models.CharField(max_length=256, default='Israel'),
            preserve_default=False,
        ),
    ]
