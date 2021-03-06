# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-28 11:32
from __future__ import unicode_literals

from django.db import migrations


def run_migration(apps, schema_editor):
    """Ensure all users have unique emails."""
    Component = apps.get_model('trans', 'Component')
    for target in Component.objects.filter(repo__startswith='weblate:'):
        project, component = target.repo[10:].split('/', 1)
        target.linked_component = Component.objects.get(
            slug=component, project__slug=project
        )
        target.save()


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0141_component_linked_component'),
    ]

    operations = [
        migrations.RunPython(run_migration)
    ]
