# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-29 08:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0005_auto_20181011_1537'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]
