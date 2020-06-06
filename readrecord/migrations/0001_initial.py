# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-08-19 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=20)),
                ('bookName', models.CharField(max_length=60)),
                ('bookId', models.IntegerField()),
                ('starthtmlPath', models.CharField(max_length=40)),
                ('startparagraphId', models.IntegerField()),
                ('startelementId', models.IntegerField()),
                ('startcharId', models.IntegerField()),
                ('endhtmlPath', models.CharField(max_length=40)),
                ('endparagraphId', models.IntegerField()),
                ('endelementId', models.IntegerField()),
                ('endcharId', models.IntegerField()),
                ('content', models.TextField()),
                ('origContent', models.TextField()),
                ('timestamp', models.IntegerField()),
                ('state', models.IntegerField()),
                ('annotationId', models.IntegerField()),
            ],
            options={
                'db_table': 'annotation',
                'verbose_name': '\u4e66\u6458\u6279\u6ce8',
                'verbose_name_plural': '\u4e66\u6458\u6279\u6ce8',
            },
        ),
        migrations.CreateModel(
            name='readprogress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=20)),
                ('bookName', models.CharField(max_length=60)),
                ('bookId', models.BigIntegerField()),
                ('progress', models.IntegerField()),
                ('readTime', models.IntegerField()),
                ('readCount', models.IntegerField()),
                ('startTime', models.BigIntegerField()),
                ('endTime', models.BigIntegerField()),
                ('wordCount', models.BigIntegerField()),
                ('pageCount', models.IntegerField()),
            ],
            options={
                'db_table': 'readprogress',
                'verbose_name': '\u9605\u8bfb\u8fdb\u5ea6',
                'verbose_name_plural': '\u9605\u8bfb\u8fdb\u5ea6',
            },
        ),
        migrations.CreateModel(
            name='recentbooklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=20)),
                ('bookName', models.CharField(max_length=100)),
                ('bookId', models.IntegerField()),
                ('bookFormat', models.CharField(max_length=15)),
                ('htmlPath', models.CharField(max_length=50)),
                ('paragraphId', models.IntegerField()),
                ('elementId', models.IntegerField()),
                ('charId', models.IntegerField()),
                ('pageId', models.IntegerField()),
                ('content', models.TextField()),
                ('timestamp', models.IntegerField(default=0)),
                ('state', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'recentbooklist',
                'verbose_name': '\u6700\u8fd1\u9605\u8bfb\u7684\u56fe\u4e66',
                'verbose_name_plural': '\u6700\u8fd1\u9605\u8bfb\u7684\u56fe\u4e66',
            },
        ),
    ]