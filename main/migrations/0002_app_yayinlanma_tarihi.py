# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='yayinlanma_tarihi',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
