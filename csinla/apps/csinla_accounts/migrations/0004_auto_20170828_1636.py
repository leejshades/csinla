# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csinla_accounts', '0003_auto_20170817_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstudentsubmission',
            name='url',
            field=models.URLField(blank=True, default='', max_length=1000, null=True, verbose_name='\u6587\u7ae0\u94fe\u63a5'),
        ),
    ]
