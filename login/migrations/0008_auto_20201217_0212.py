# Generated by Django 2.2 on 2020-12-17 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20201217_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplot',
            name='radio',
            field=models.CharField(choices=[('r', 'red'), ('g', 'green'), ('b', 'blue')], default='r', max_length=30),
        ),
    ]
