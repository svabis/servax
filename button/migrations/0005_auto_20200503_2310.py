# Generated by Django 2.2 on 2020-05-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('button', '0004_auto_20200503_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='url',
            field=models.SlugField(default='72bff3937846', unique=True),
        ),
    ]
