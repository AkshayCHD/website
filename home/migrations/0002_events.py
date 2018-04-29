# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-28 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, null=True)),
                ('brief', models.CharField(max_length=500, null=True)),
                ('url', models.URLField(db_index=True, max_length=128, null=True)),
            ],
        ),
    ]
