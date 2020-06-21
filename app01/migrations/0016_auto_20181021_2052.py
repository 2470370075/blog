# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-21 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_auto_20181021_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='up',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(null=True, upload_to='avatars/', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]