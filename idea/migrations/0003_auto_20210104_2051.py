# Generated by Django 2.2 on 2021-01-04 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_auto_20210104_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supertheme',
            name='color',
            field=models.CharField(blank=True, default='', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='supertheme',
            name='icon',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]