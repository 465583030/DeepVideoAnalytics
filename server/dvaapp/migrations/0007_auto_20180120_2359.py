# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-20 23:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0006_trainingset_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainedmodel',
            old_name='source',
            new_name='event',
        ),
    ]
