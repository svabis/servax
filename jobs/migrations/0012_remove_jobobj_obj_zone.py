# Generated by Django 2.2 on 2021-01-29 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_jobobj_zone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobobj',
            name='obj_zone',
        ),
    ]
