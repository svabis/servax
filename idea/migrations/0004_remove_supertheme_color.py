# Generated by Django 2.2 on 2021-01-04 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0003_auto_20210104_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supertheme',
            name='color',
        ),
    ]