# Generated by Django 2.2 on 2020-03-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smhouse', '0010_auto_20200322_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termoplace',
            name='regex',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]