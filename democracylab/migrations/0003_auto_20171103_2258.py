# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-03 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('democracylab', '0002_auto_20171028_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='postal_code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]