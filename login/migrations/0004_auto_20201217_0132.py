# Generated by Django 2.2 on 2020-12-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_mapplot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapplot',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='mapplot',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
    ]
