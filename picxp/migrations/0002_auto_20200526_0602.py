# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-26 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picxp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name']},
        ),
    ]