# Generated by Django 4.2 on 2023-04-09 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_job_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='content',
            new_name='experience',
        ),
    ]
