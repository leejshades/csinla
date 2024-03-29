# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-28 09:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('csinla_posts', '0005_auto_20170828_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='\u4e8c\u624b', max_length=128, verbose_name='\u6807\u7b7e\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 27, 9, 22, 29, 271000, tzinfo=utc), verbose_name='\u5230\u671f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='used',
            name='tags',
            field=models.ManyToManyField(blank=True, default='\u4e8c\u624b', null=True, to='csinla_posts.UsedTag', verbose_name='\u6807\u7b7e'),
        ),
    ]
