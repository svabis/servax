# Generated by Django 2.2 on 2021-04-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_camera_online_cam_05'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='cam_subfolder',
            field=models.CharField(default='', max_length=60),
        ),
    ]
