# Generated by Django 2.2 on 2020-12-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobs_jobs_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='jobs_link',
            field=models.URLField(blank=True, null=True, verbose_name='Saite'),
        ),
    ]
