# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20161212_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]