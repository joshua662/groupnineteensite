# Generated by Django 4.2.8 on 2025-06-15 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0010_assignedtask_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='crud.section'),
        ),
    ]
