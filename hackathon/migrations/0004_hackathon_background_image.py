# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_auto_20170719_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='hackathon arkaplan resmi'),
        ),
    ]