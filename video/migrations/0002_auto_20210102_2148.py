# Generated by Django 2.2 on 2021-01-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='cam_color',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='camera',
            name='cam_icon',
            field=models.CharField(default='', max_length=50),
        ),
    ]