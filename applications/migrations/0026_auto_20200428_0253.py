# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-28 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0025_auto_20200427_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentorapplication',
            old_name='projects',
            new_name='participated',
        ),
    ]
