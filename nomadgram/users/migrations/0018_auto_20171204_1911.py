# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-04 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20171204_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('not-specified', 'Not specified'), ('male', 'Male'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]
