# Generated by Django 2.2 on 2021-01-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0005_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
