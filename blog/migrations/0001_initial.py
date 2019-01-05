# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-05 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='博客标题')),
                ('category', models.CharField(blank=True, max_length=20, verbose_name='博客标签')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('update_date', models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-pub_date'],
            },
        ),
    ]
