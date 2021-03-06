# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-09 14:05
from __future__ import unicode_literals

from django.db import migrations, models

from weblate.formats.models import FILE_FORMATS



class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0124_auto_20180215_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change',
            name='action',
            field=models.IntegerField(choices=[(0, 'Resource update'), (1, 'Translation completed'), (2, 'Translation changed'), (5, 'New translation'), (3, 'Comment added'), (4, 'Suggestion added'), (6, 'Automatic translation'), (7, 'Suggestion accepted'), (8, 'Translation reverted'), (9, 'Translation uploaded'), (10, 'Glossary added'), (11, 'Glossary updated'), (12, 'Glossary uploaded'), (13, 'New source string'), (14, 'Component locked'), (15, 'Component unlocked'), (16, 'Detected duplicate string'), (17, 'Committed changes'), (18, 'Pushed changes'), (19, 'Reset repository'), (20, 'Merged repository'), (21, 'Rebased repository'), (22, 'Failed merge on repository'), (23, 'Failed rebase on repository'), (28, 'Failed push on repository'), (24, 'Parse error'), (25, 'Removed translation'), (26, 'Suggestion removed'), (27, 'Search and replace'), (29, 'Suggestion removed during cleanup'), (30, 'Source string changed'), (31, 'New string added')], default=2),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='file_format',
            field=models.CharField(choices=FILE_FORMATS.get_choices(), default='auto', help_text='Automatic detection might fail for some formats and is slightly slower.', max_length=50, verbose_name='File format'),
        ),
    ]
