# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-05-21 11:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_blacklist_and_user_type_permisions_20200520_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='token', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]