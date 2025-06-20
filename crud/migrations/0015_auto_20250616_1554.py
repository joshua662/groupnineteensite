# Generated by Django 4.2.8 on 2025-06-16 15:54

from django.db import migrations, models

def create_sections(apps, schema_editor):
    Section = apps.get_model('crud', 'Section')
    sections_to_create = ['A', 'B', 'C', 'D']
    for section_name in sections_to_create:
        Section.objects.get_or_create(name=section_name)


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0014_assignedtask_submitted_at'),
    ]

    operations = [
        migrations.RunPython(create_sections),
    ]
