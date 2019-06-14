# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-14 18:22
from __future__ import unicode_literals

import ckeditor.fields
import cms.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CmsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('route', models.CharField(max_length=200, verbose_name='Путь')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='CmsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('is_permited', models.BooleanField(default=False, verbose_name='Сделать закрытым')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cms.CmsCategory', verbose_name='Категория')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'permissions': (('moderate_cmspost', 'Модерация постов'), ('permited_access', 'Просмотр закрытых постов')),
            },
        ),
        migrations.CreateModel(
            name='CmsProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=cms.utils.PathAndRename('avatars/'), verbose_name='Аватар')),
                ('birth_date', models.CharField(blank=True, max_length=80, null=True, verbose_name='Дата рождения')),
                ('location', models.CharField(blank=True, max_length=80, null=True, verbose_name='Местоположение')),
                ('facebook', models.CharField(blank=True, max_length=80, null=True, verbose_name='Facebook')),
                ('vk', models.CharField(blank=True, max_length=80, null=True, verbose_name='Vkontakte')),
                ('instagram', models.CharField(blank=True, max_length=80, null=True, verbose_name='Instagram')),
                ('twitter', models.CharField(blank=True, max_length=80, null=True, verbose_name='Twitter')),
                ('youtube', models.CharField(blank=True, max_length=80, null=True, verbose_name='YouTube')),
                ('telegram', models.CharField(blank=True, max_length=80, null=True, verbose_name='Telegram')),
                ('skype', models.CharField(blank=True, max_length=80, null=True, verbose_name='Skype')),
                ('last_activity', models.DateTimeField(blank=True, null=True, verbose_name='Был в сети')),
                ('email_change_token', models.CharField(max_length=42, verbose_name='Код подтверждения смены e-mail')),
                ('new_email', models.CharField(max_length=256, verbose_name='Новый e-mail')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=600, verbose_name='Текст')),
                ('is_moderated', models.BooleanField(default=True, verbose_name='Подтвержден модератором')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удален')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, unique=True, verbose_name='Дата создания')),
                ('modifed_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.Comment', verbose_name='Ответ на')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.CmsPost', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'permissions': (('moderate_comment', 'Модерация комментариев'),),
            },
        ),
    ]
