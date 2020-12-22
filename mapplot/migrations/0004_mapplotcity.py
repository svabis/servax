# Generated by Django 2.2 on 2020-12-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapplot', '0003_auto_20201218_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapPlotCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
            options={
                'db_table': 'map_plot_city',
            },
        ),
    ]
