# Generated by Django 2.2 on 2021-04-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20210111_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera_online',
            name='cam_05',
            field=models.BooleanField(default=False),
        ),
    ]