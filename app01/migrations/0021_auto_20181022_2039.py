# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-22 12:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0020_auto_20181022_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('tagtitle', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(null=True, to='app01.Tag'),
        ),
    ]