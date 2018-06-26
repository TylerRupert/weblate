# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 13:00
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('legal', '0001_initial'), ('legal', '0002_auto_20170821_1704'), ('legal', '0003_auto_20180416_1405'), ('legal', '0004_copy_auditlog')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tos', models.DateField(default=datetime.date(1970, 1, 1))),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('address', models.GenericIPAddressField(null=True)),
                ('user_agent', models.CharField(default='', max_length=200)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
    ]