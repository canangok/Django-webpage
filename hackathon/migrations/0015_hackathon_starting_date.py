# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0014_hackathon_directions'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='starting_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Başlangıç Tarihi'),
        ),
    ]
