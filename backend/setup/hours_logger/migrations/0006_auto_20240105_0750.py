# Generated by Django 3.2.19 on 2024-01-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hours_logger', '0005_auto_20240101_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='start',
            field=models.DateTimeField(null=True),
        ),
    ]