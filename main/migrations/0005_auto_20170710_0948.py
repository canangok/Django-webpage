# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 06:48
from __future__ import unicode_literals

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_imageexamplemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageExampleModel',
        ),
        migrations.RemoveField(
            model_name='app',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='app',
            name='width_field',
        ),
        migrations.AddField(
            model_name='app',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Height'),
        ),
        migrations.AddField(
            model_name='app',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Width'),
        ),
        migrations.AlterField(
            model_name='app',
            name='background_image',
            field=versatileimagefield.fields.VersatileImageField(height_field='height', upload_to='', verbose_name='Arkaplan resmi', width_field='width'),
        ),
    ]