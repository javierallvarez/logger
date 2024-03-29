# Generated by Django 3.2.9 on 2022-02-25 10:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('log_wow', '0004_auto_20220224_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('hour', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]
