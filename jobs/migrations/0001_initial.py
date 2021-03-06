# Generated by Django 3.0.3 on 2020-03-01 07:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobObj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_added', models.DateField(default=datetime.datetime.now, verbose_name='Darbs pievienots')),
                ('obj_title', models.CharField(max_length=50)),
                ('obj_descr', models.TextField(blank=True)),
                ('obj_actual', models.BooleanField(default=False)),
                ('obj_zone', models.CharField(choices=[('maja', 'māja'), ('IT', 'IT'), ('lapene', 'lapene'), ('skjunis', 'šķūnis'), ('elektriba', 'elektrība'), ('santehnika', 'santehnika'), ('instrument', 'instrumenti'), ('darzs', 'dārzs'), ('zogs', 'žogs'), ('grods', 'grods'), ('koki', 'koki'), ('cits', 'cits')], default='cits', max_length=10)),
                ('obj_url', models.URLField(blank=True, null=True)),
                ('obj_nr', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'job_objects',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobs_date_added', models.DateField(default=datetime.datetime.now, verbose_name='Darbs pievienots')),
                ('jobs_date_done', models.DateField(blank=True, null=True)),
                ('jobs_date_start', models.DateField(blank=True, null=True, verbose_name='Darbs uzsākts')),
                ('jobs_descr', models.TextField(verbose_name='Darba uzdevums')),
                ('jobs_zone', models.CharField(choices=[('maja', 'māja'), ('IT', 'IT'), ('lapene', 'lapene'), ('skjunis', 'šķūnis'), ('elektriba', 'elektrība'), ('santehnika', 'santehnika'), ('instrument', 'instrumenti'), ('darzs', 'dārzs'), ('zogs', 'žogs'), ('grods', 'grods'), ('koki', 'koki'), ('cits', 'cits')], default='IT', max_length=10, verbose_name='Darba zona')),
                ('jobs_type', models.CharField(choices=[('ATRAST', 'atrast'), ('JADARA', 'jādara'), ('PETIT', 'izpētīt apdomāt'), ('JAPERK', 'jāpērk'), ('VEST', 'transports'), ('SVARIGI', 'svarīgi'), ('KUVALDA', 'TrailCamPhoto'), ('GRAVANI', 'IT-Projekti')], default='JADARA', max_length=10, verbose_name='Darba veids/svarīgums')),
                ('jobs_done', models.BooleanField(default=False)),
                ('jobs_cancel', models.BooleanField(default=False)),
                ('marked', models.BooleanField(default=False)),
                ('marked_until', models.DateField(blank=True, null=True, verbose_name='Izcelts līdz')),
                ('marked_id', models.IntegerField(blank=True, null=True, verbose_name='Izcelts Nr.p.k.')),
                ('jobs_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='JobObj_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_image_big', models.ImageField(blank=True, null=True, upload_to='job_obj/big/')),
                ('obj_image_small', models.ImageField(blank=True, null=True, upload_to='job_obj/')),
                ('job_obj', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='o_i', to='jobs.JobObj')),
            ],
            options={
                'db_table': 'job_objects_images',
            },
        ),
        migrations.CreateModel(
            name='JobObj_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_file', models.FileField(blank=True, null=True, upload_to='job_obj/file/')),
                ('job_obj', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='o_f', to='jobs.JobObj')),
            ],
            options={
                'db_table': 'job_objects_files',
            },
        ),
    ]
