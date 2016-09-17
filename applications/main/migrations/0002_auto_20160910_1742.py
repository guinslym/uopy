# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubevent',
            name='event_end',
        ),
        migrations.RemoveField(
            model_name='clubevent',
            name='event_start',
        ),
        migrations.AddField(
            model_name='clubevent',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='event date'),
            preserve_default=False,
        ),
    ]