# Generated by Django 2.2 on 2021-05-09 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_camera_cam_subfolder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='cam_subfolder',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
    ]
