# Generated by Django 2.2 on 2021-03-29 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_auto_20210130_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='jobs_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='jobs.JobsTypes'),
        ),
    ]