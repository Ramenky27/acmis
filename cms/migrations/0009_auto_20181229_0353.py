# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-29 01:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20181216_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='binarypost',
            options={'permissions': (('moderate_binarypost', 'Модерація зображень'),), 'verbose_name': 'Зображення', 'verbose_name_plural': 'Зображеняя'},
        ),
        migrations.AlterModelOptions(
            name='cmspost',
            options={'permissions': (('moderate_cmspost', 'Модерація постів'), ('publish_cmspost', 'Оприлюднення постів')), 'verbose_name': 'Пост', 'verbose_name_plural': 'Пости'},
        ),
        migrations.AlterModelOptions(
            name='cmsprofile',
            options={'permissions': (('moderate_cmsprofile', 'Модерація профілів'),), 'verbose_name': 'Профіль', 'verbose_name_plural': 'Профілі'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('moderate_comment', 'Модерація коментарів'),), 'verbose_name': 'Коментар', 'verbose_name_plural': 'Коментарі'},
        ),
        migrations.AlterModelOptions(
            name='forumgroups',
            options={'permissions': (('change_forumn_access', 'Зміна доступа до прихованих розділів форума '),), 'verbose_name': 'Групи форума', 'verbose_name_plural': 'Группи форума'},
        ),
        migrations.AlterModelOptions(
            name='textpost',
            options={'permissions': (('moderate_textpost', 'Модерація текстових постів'),), 'verbose_name': 'Текстовий пост', 'verbose_name_plural': 'Текстові пости'},
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='allow_anonymous',
            field=models.BooleanField(default=True, help_text='Встановлення цієї галочки відключає контроль доступа за группами користувачів', verbose_name='Повний доступ'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Группи, що мають доступ'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='i18n_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Переклад назви'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='i18n_name_plural',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Переклад назви у множинному числі'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='kind',
            field=models.CharField(choices=[('0', 'Файл'), ('1', 'Пост'), ('3', 'Не визначено')], default='3', help_text='<font color="red">Увага! Зміна цього поля для існуючих категорій може вплинути на відображення об\'єктів!</font>', max_length=254, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='cmscategory',
            name='route',
            field=models.CharField(help_text='<font color="red">Увага! Зміна цього поля для існуючих категорій може вплинути на логіку роботи!</font>', max_length=200, verbose_name='Шлях URL'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='is_moderated',
            field=models.BooleanField(default=True, verbose_name='Схвалено'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='Оприлюднено'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='cmspost',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='birth_date',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='last_activity',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Був онлайн'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='location',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Місцезнаходження'),
        ),
        migrations.AlterField(
            model_name='cmsprofile',
            name='site',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Сайт'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, unique=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Видалено'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_moderated',
            field=models.BooleanField(default=True, verbose_name='Схвалено'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modifed_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата редагування'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.Comment', verbose_name='Відповідь на'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.CmsPost', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='emailchange',
            name='auth_key',
            field=models.CharField(max_length=42, verbose_name='Код підтвердження'),
        ),
        migrations.AlterField(
            model_name='emailchange',
            name='new_email',
            field=models.CharField(max_length=256, verbose_name='Новий e-mail'),
        ),
        migrations.AlterField(
            model_name='forumgroups',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Групи з доступом до прихованих розділів форума'),
        ),
    ]