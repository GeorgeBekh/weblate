# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0016_auto_20141208_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='check',
            field=models.CharField(max_length=20, choices=[('end_space', 'Trailing space'), ('begin_space', 'Starting spaces'), ('python_brace_format', 'Python brace format'), ('plurals', 'Missing plurals'), ('escaped_newline', 'Mismatched \\n'), ('end_exclamation', 'Trailing exclamation'), ('php_format', 'PHP format'), ('same', 'Unchanged translation'), ('xml-tags', 'XML tags mismatch'), ('bbcode', 'Mismatched BBcode'), ('zero-width-space', 'Zero-width space'), ('c_format', 'C format'), ('end_colon', 'Trailing colon'), ('end_question', 'Trailing question'), ('end_ellipsis', 'Trailing ellipsis'), ('end_stop', 'Trailing stop'), ('begin_newline', 'Starting newline'), ('inconsistent', 'Inconsistent'), ('end_newline', 'Trailing newline'), ('python_format', 'Python format')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='mail',
            field=models.EmailField(help_text='Mailing list for translators.', max_length=254, verbose_name='Mailing list', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subproject',
            name='committer_email',
            field=models.EmailField(default='noreply@weblate.org', max_length=254, verbose_name='Committer email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subproject',
            name='report_source_bugs',
            field=models.EmailField(help_text='Email address where errors in source string will be reported, keep empty for no emails.', max_length=254, verbose_name='Source string bug report address', blank=True),
            preserve_default=True,
        ),
    ]
