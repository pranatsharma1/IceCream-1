# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-31 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0018_auto_20160801_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='contact',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
