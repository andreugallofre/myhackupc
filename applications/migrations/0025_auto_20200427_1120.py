# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-27 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0024_remove_sponsorapplication_which_hack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorapplication',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='degree',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='study_work',
            field=models.BooleanField(max_length=300),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='university',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mentorapplication',
            name='which_hack',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'HackAssistant 2016'), (1, 'HackAssistant 2017'), (2, 'HackAssistant 2018'), (3, 'HackAssistant 2019')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='which_hack',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'HackAssistant 2016'), (1, 'HackAssistant 2017'), (2, 'HackAssistant 2018'), (3, 'HackAssistant 2019')], max_length=7, null=True),
        ),
    ]
