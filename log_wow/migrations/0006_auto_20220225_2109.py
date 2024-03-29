# Generated by Django 3.2.9 on 2022-02-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_wow', '0005_auto_20220225_1008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
