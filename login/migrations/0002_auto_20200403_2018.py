# Generated by Django 2.2 on 2020-04-03 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_video',
            name='leave',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
