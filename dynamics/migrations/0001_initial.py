# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('numb', models.IntegerField(max_length=11)),
            ],
        ),
    ]