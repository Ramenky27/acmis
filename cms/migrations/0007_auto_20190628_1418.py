# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-28 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20190628_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='file',
            field=models.ImageField(upload_to='maps/', verbose_name='Файл'),
        ),
    ]