# Generated by Django 2.2 on 2020-12-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0007_mapplot_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapplot',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mapplot',
            name='unique',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mapplot',
            name='radio',
            field=models.CharField(choices=[('yellow', 'sarkans'), ('green', 'zaļš'), ('blue', 'zils')], default='red', max_length=10),
        ),
    ]
