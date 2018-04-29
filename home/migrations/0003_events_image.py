# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-28 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='events_images/'),
            preserve_default=False,
        ),
    ]
