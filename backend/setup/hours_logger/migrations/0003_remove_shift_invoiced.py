# Generated by Django 3.2.19 on 2024-01-01 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hours_logger', '0002_auto_20231229_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='invoiced',
        ),
    ]
