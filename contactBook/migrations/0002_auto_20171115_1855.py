# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactBook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(default='N', max_length=1),
        ),
    ]