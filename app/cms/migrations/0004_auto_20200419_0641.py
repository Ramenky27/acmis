# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-19 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_cmspost_last_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmspost',
            name='last_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Comment', verbose_name='Останній коментар'),
        ),
    ]
