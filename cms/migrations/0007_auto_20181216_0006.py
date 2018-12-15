# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-15 22:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20180712_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='binarypost',
            options={'permissions': (('moderate_binarypost', 'Moderate images posts'),), 'verbose_name': 'Image post', 'verbose_name_plural': 'Images posts'},
        ),
        migrations.AlterModelOptions(
            name='cmscategory',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='cmspost',
            options={'permissions': (('moderate_cmspost', 'Moderate posts'), ('publish_cmspost', 'Publish posts')), 'verbose_name': 'Повідомлення', 'verbose_name_plural': 'Повідомлення'},
        ),
        migrations.AlterModelOptions(
            name='cmsprofile',
            options={'permissions': (('moderate_cmsprofile', 'Moderate profiles'),), 'verbose_name': 'Профіль', 'verbose_name_plural': 'Профілі'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('moderate_comment', 'Moderate comments'),), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='forumgroups',
            options={'permissions': (('change_forumn_access', 'Change aditional access to forum'),), 'verbose_name': 'Forum group', 'verbose_name_plural': 'Forum groups'},
        ),
        migrations.AlterModelOptions(
            name='textpost',
            options={'permissions': (('moderate_textpost', 'Moderate text post'),), 'verbose_name': 'Text post', 'verbose_name_plural': 'Text posts'},
        ),
        migrations.AlterField(
            model_name='binarypost',
            name='description',
            field=models.TextField(blank=True, max_length=200, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='allow_anonymous',
            field=models.BooleanField(default=True, help_text='Setting this checkbox disables access control to categories by user group.', verbose_name='Full access'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Groups with access'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='i18n_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='i18n name'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='i18n_name_plural',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='i18n name plural'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='kind',
            field=models.CharField(choices=[('0', 'Файл'), ('1', 'Повідомлення'), ('3', 'Невідомо')], default='3', help_text='<font color="red">Attention! Changing this field in existing categories may affect the display of objects!</font>', max_length=254, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='name',
            field=models.CharField(max_length=200, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='route',
            field=models.CharField(help_text='<font color="red">Attention! Changing this field in existing categories may affect the logic!</font>', max_length=200, verbose_name='Route'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.CmsCategory', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='is_moderated',
            field=models.BooleanField(default=True, verbose_name='Approved'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='birth_date',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Birth date'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='last_activity',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last online'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='location',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='site',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Site'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, unique=True, verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Deleted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_moderated',
            field=models.BooleanField(default=True, verbose_name='Approved'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modifed_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Dete edited'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.Comment', verbose_name='Reply to'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.CmsPost', verbose_name='Повідомлення'),
        ),
        migrations.AlterField(
            model_name='emailchange',
            name='auth_key',
            field=models.CharField(max_length=42, verbose_name='Confirmation code'),
        ),
        migrations.AlterField(
            model_name='emailchange',
            name='new_email',
            field=models.CharField(max_length=256, verbose_name='New email'),
        ),
        migrations.AlterField(
            model_name='emailchange',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач'),
        ),
        migrations.AlterField(
            model_name='forumgroups',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Groups with aditional access to forum'),
        ),
    ]