# Generated by Django 2.2 on 2021-05-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_auto_20210514_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='server_task',
            name='task_done_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]