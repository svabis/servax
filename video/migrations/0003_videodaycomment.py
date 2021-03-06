# Generated by Django 2.2 on 2021-01-11 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20210102_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoDayComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('comment', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'video_day_comment',
            },
        ),
    ]
