# Generated by Django 2.2 on 2021-01-29 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_auto_20210129_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='jobs_zone',
        ),
    ]
