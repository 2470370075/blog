# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-04 15:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0028_auto_20181103_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updown',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.IntegerField(max_length=5, null=True)),
                ('article', models.IntegerField(max_length=5, null=True)),
                ('updown', models.IntegerField(max_length=5, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='updown',
            unique_together=set([('user', 'article')]),
        ),
    ]
