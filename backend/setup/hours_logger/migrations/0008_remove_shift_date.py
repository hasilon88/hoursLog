# Generated by Django 3.2.19 on 2024-01-05 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hours_logger', '0007_pauselog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='date',
        ),
    ]
