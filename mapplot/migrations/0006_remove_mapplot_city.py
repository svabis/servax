# Generated by Django 2.2 on 2020-12-18 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0005_auto_20201218_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapplot',
            name='city',
        ),
    ]
