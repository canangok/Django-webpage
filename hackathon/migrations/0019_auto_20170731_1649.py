# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0018_auto_20170726_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook link'),
        ),
        migrations.AddField(
            model_name='committee',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter link'),
        ),
    ]
