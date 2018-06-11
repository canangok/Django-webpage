# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Kişi ismi')),
                ('title', models.CharField(max_length=255, verbose_name='Ünvanı')),
                ('business', models.CharField(max_length=255, verbose_name='Firma/Şirket')),
                ('mentor', models.BooleanField(default=False, verbose_name='Mentor')),
                ('jury', models.BooleanField(default=False, verbose_name='Juri')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
            ],
            options={
                'verbose_name': 'Juri ve Mentor',
                'verbose_name_plural': 'Juriler ve Mentorler',
            },
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='', verbose_name='hackathon ikonu')),
                ('main_image', models.ImageField(upload_to='', verbose_name='Arkaplan resmi')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('slogan', models.CharField(max_length=255, verbose_name='Slogan')),
                ('date', models.CharField(max_length=255, verbose_name='Tarih')),
                ('place', models.CharField(max_length=255, verbose_name='Yer')),
                ('description', models.TextField(verbose_name='Açıklama')),
                ('address', models.TextField(verbose_name='Adres')),
                ('email', models.EmailField(max_length=254, verbose_name='E-posta')),
                ('phone', models.CharField(blank=True, default='', max_length=20, verbose_name='Telefon')),
            ],
            options={
                'verbose_name': 'Hackathon',
                'verbose_name_plural': 'Hackathonlar',
            },
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Menü ismi')),
                ('order', models.CharField(blank=True, default='', max_length=10, verbose_name='Sırası')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.Hackathon')),
            ],
            options={
                'verbose_name': 'Menü',
                'verbose_name_plural': 'Menüler',
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ödül ismi')),
                ('order', models.CharField(blank=True, default='', max_length=3, verbose_name='Ödül Sırası')),
                ('icon', models.ImageField(upload_to='', verbose_name='Ödül ikonu')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.Hackathon')),
            ],
            options={
                'verbose_name': 'Ödül',
                'verbose_name_plural': 'Ödüller',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, '1. Gün'), (2, '2. Gün'), (3, '3. Gün')], default=1)),
                ('time_interval', models.CharField(max_length=255, verbose_name='Zaman aralığı')),
                ('order', models.CharField(blank=True, default='', max_length=10, verbose_name='Sırası')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.Hackathon')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programlar',
            },
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='', verbose_name='sponsor ikonu')),
                ('name', models.CharField(max_length=255, verbose_name='Sponsor ismi')),
                ('description', models.TextField(verbose_name='Sponsor açıklama')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.Hackathon')),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsorlar',
            },
        ),
        migrations.CreateModel(
            name='Sss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Soru')),
                ('answer', models.TextField(verbose_name='Cevap')),
                ('order', models.CharField(blank=True, default='', max_length=10, verbose_name='Soru sırası')),
                ('hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.Hackathon')),
            ],
            options={
                'verbose_name': 'Sık Sorulan Soru',
                'verbose_name_plural': 'Sık Sorulan Sorular',
            },
        ),
        migrations.AddField(
            model_name='committee',
            name='hackathon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hackathon.Hackathon'),
        ),
    ]
