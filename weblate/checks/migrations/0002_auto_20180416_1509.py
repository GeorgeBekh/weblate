# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lang', '0011_auto_20180215_1158'),
        ('trans', '0130_auto_20180416_1503'),
        ('checks', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='check',
            unique_together=set([('content_hash', 'project', 'language', 'check')]),
        ),
        migrations.AlterIndexTogether(
            name='check',
            index_together=set([('project', 'language', 'content_hash')]),
        ),
    ]
