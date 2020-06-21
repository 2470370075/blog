# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-22 04:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_auto_20181021_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='theme',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
