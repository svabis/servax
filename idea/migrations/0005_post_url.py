# Generated by Django 2.2 on 2021-01-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0004_remove_supertheme_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]