# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0002_hackathon_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='main_image',
            field=models.ImageField(upload_to='', verbose_name='hackathon resmi'),
        ),
    ]
